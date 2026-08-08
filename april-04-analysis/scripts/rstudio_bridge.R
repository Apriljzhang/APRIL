# APRIL Stage 04: supervised local RStudio execution bridge
# Adapted from brucehu-create/rstudio-bridge at commit
# fdbfbb05cae3cb5fa914b9ea1f7b5ac9905b68e2 under the MIT licence retained
# in rstudio-bridge-LICENSE.txt.
# Dependencies: httpuv, jsonlite, rstudioapi (optional source/plot integration)

#' Start APRIL's supervised RStudio bridge
#'
#' Launch an authenticated httpuv server on localhost that allows APRIL to
#' execute R code, inspect objects, and push data into the R environment.
#'
#' Features:
#' * Agent code is appended live to a source file opened in the RStudio
#'   source pane (real-time supervision).
#' * Plot-producing code is auto-printed so figures appear in the RStudio
#'   Plots pane.
#' * New environment variables are checked against a readable naming
#'   convention, with warnings returned to the agent.
#' * Every eval / attach refresh updates an `april_environment_guide.md` file that
#'   documents each variable in the global environment (name, type, dims,
#'   and a human-readable description).
#'
#' @param port Integer. Port to listen on (default: 8765L)
#' @param host Character. Must remain "127.0.0.1".
#' @param token Character. Shared secret sent in the X-APRIL-Token header.
#'   Defaults to APRIL_RSTUDIO_TOKEN and must contain at least 16 characters.
#' @param max_rows Integer. Maximum data-frame rows returned by /data.
#' @param history_file Character. Path to the audit trail file.
#' @param source_file Character. Path to the live source file opened in the
#'   RStudio source pane. Defaults to `april_agent_code.R` in the working dir.
#' @param guide_file Character. Path to the environment-variable guide file.
#'   Defaults to `april_environment_guide.md` in the working dir.
#' @param quiet Logical. Suppress startup message if TRUE
#'
#' @return Invisibly returns the server object
#' @export
#'
#' @examples
#' \dontrun{
#'   Sys.setenv(APRIL_RSTUDIO_TOKEN = "replace-with-a-long-random-token")
#'   april_bridge <- april_start_rstudio_bridge()
#' }
april_start_rstudio_bridge <- function(
    port = 8765L,
    host = "127.0.0.1",
    token = Sys.getenv("APRIL_RSTUDIO_TOKEN", unset = ""),
    max_rows = 1000L,
    history_file = NULL,
    source_file = NULL,
    guide_file = NULL,
    quiet = FALSE) {

  if (!identical(host, "127.0.0.1")) {
    stop("APRIL's RStudio bridge must bind to 127.0.0.1 only.",
         call. = FALSE)
  }
  if (!is.character(token) || length(token) != 1L || nchar(token) < 16L) {
    stop("Set APRIL_RSTUDIO_TOKEN to a secret of at least 16 characters.",
         call. = FALSE)
  }
  if (length(port) != 1L || is.na(port) || port < 1024L || port > 65535L) {
    stop("port must be one integer from 1024 through 65535.", call. = FALSE)
  }
  if (length(max_rows) != 1L || is.na(max_rows) || max_rows < 1L) {
    stop("max_rows must be a positive integer.", call. = FALSE)
  }

  required_packages <- c("httpuv", "jsonlite")
  missing_packages <- required_packages[
    !vapply(required_packages, requireNamespace, quietly = TRUE,
            FUN.VALUE = logical(1))
  ]
  if (length(missing_packages) > 0L) {
    stop(
      "Install required R package(s) explicitly before starting the bridge: ",
      paste(missing_packages, collapse = ", "),
      call. = FALSE
    )
  }

  # ---- Paths ----
  if (is.null(history_file)) {
    history_file <- file.path(getwd(), "april_agent_code_history.R")
  }
  if (is.null(source_file)) {
    source_file <- file.path(getwd(), "april_agent_code.R")
  }
  if (is.null(guide_file)) {
    guide_file <- file.path(getwd(), "april_environment_guide.md")
  }

  ensure_file <- function(path, header_lines = NULL) {
    if (!file.exists(path)) {
      lines <- c(header_lines, "")
      writeLines(na.omit(lines), path)
    }
  }
  ensure_file(history_file, c("# APRIL RStudio Bridge — Code Audit Trail",
                              paste0("# Created: ", Sys.time())))
  ensure_file(source_file, c("# APRIL RStudio Bridge — Live Agent Code",
                             "# This file is auto-updated as the agent works.",
                             paste0("# Created: ", Sys.time())))

  # Whether rstudioapi is usable for live source/plots sync
  use_rstudio <- requireNamespace("rstudioapi", quietly = TRUE) &&
    rstudioapi::isAvailable()

  # Registry of human-readable descriptions for environment variables
  var_descriptions <- new.env(parent = emptyenv())

  # ---- Helpers ----

  append_to_history <- function(code) {
    timestamp <- format(Sys.time(), "%Y-%m-%d %H:%M:%S")
    entry <- paste0("\n# [", timestamp, "]\n", code, "\n")
    cat(entry, file = history_file, append = TRUE)
    invisible(NULL)
  }

  # Append code to the live source file AND refresh it in the RStudio
  # source pane so the human can watch it in real time.
  append_to_source <- function(code) {
    if (!file.exists(source_file)) ensure_file(source_file)
    timestamp <- format(Sys.time(), "%H:%M:%S")
    entry <- paste0("\n# --- ", timestamp, " ---\n", code, "\n")
    cat(entry, file = source_file, append = TRUE)

    if (!use_rstudio) return(invisible(NULL))
    # Refresh the open document in RStudio
    tryCatch({
      new_content <- paste(readLines(source_file, warn = FALSE), collapse = "\n")
      ids <- rstudioapi::documentIdAll(which = "open")
      for (id in ids) {
        ctx <- rstudioapi::documentContext(id)
        if (identical(ctx$path, source_file)) {
          rstudioapi::documentUpdate(id, contents = new_content)
          break
        }
      }
    }, error = function(e) {
      # If the doc isn't tracked, (re)open it so it becomes visible
      tryCatch(rstudioapi::documentOpen(source_file), error = function(e2) NULL)
    })
    invisible(NULL)
  }

  # Auto-print plot-producing values so they show up in the RStudio Plots pane.
  auto_print_plots <- function(value) {
    if (is.null(value)) return(invisible(NULL))
    cls <- class(value)
    is_plot <- any(c("ggplot", "recordedplot", "gg", "gtable") %in% cls) ||
      (inherits(value, "trellis")) ||
      (is.list(value) && all(c("data", "layers") %in% names(value)))
    if (is_plot) {
      tryCatch(print(value), error = function(e) NULL)
    }
    invisible(NULL)
  }

  # Check new variable names against a readable naming convention.
  check_naming <- function(vars) {
    issues <- character(0)
    for (v in vars) {
      if (v %in% c(".Random.seed", "last.warning")) next
      if (grepl("^[A-Z][A-Z0-9_]*$", v)) {
        issues <- c(issues, paste0("'", v, "' uses ALL-CAPS; use snake_case"))
      } else if (grepl("[[:space:]]", v)) {
        issues <- c(issues, paste0("'", v, "' contains spaces; use snake_case"))
      } else if (grepl("^[0-9]", v)) {
        issues <- c(issues, paste0("'", v, "' starts with a digit; rename it"))
      } else if (nchar(v) < 3) {
        issues <- c(issues, paste0("'", v, "' is a very short name; prefer descriptive"))
      }
    }
    issues
  }

  # Refresh the environment guide file documenting every global variable.
  update_env_guide <- function() {
    objs <- ls(.GlobalEnv, all.names = TRUE)
    objs <- objs[!grepl("^\\.", objs)]  # skip internal dot-vars

    lines <- c("# APRIL RStudio Bridge — Environment Guide",
               paste0("Updated: ", Sys.time()),
               "",
               "| Object | Type | Dimensions/length | Description |",
               "|---|---|---|---|")

    for (nm in objs) {
      o <- tryCatch(get(nm, envir = .GlobalEnv), error = function(e) NULL)
      if (is.null(o)) next
      desc <- if (exists(nm, envir = var_descriptions, inherits = FALSE))
        var_descriptions[[nm]] else ""
      if (nchar(desc) == 0) desc <- "(description not supplied)"

      if (inherits(o, "Seurat")) {
        type <- "Seurat"
        dims <- paste0(ncol(o), " x ", nrow(o))
      } else if (is.data.frame(o)) {
        type <- "data.frame"
        dims <- paste0(nrow(o), " x ", ncol(o))
      } else if (is.matrix(o)) {
        type <- "matrix"
        dims <- paste0(nrow(o), " x ", ncol(o))
      } else if (is.list(o)) {
        type <- "list"
        dims <- paste0("len=", length(o))
      } else if (is.atomic(o)) {
        type <- class(o)[1]
        dims <- paste0("len=", length(o))
      } else if (is.function(o)) {
        type <- "function"
        dims <- "-"
      } else {
        type <- class(o)[1]
        dims <- "-"
      }
      lines <- c(lines, sprintf("| %s | %s | %s | %s |", nm, type, dims, desc))
    }

    writeLines(lines, guide_file)
    invisible(NULL)
  }

  json_response <- function(body_data, status = 200L) {
    list(
      status = status,
      headers = list("Content-Type" = "application/json"),
      body = jsonlite::toJSON(body_data, auto_unbox = TRUE, force = TRUE)
    )
  }

  is_authorized <- function(req) {
    supplied <- req$HTTP_X_APRIL_TOKEN
    is.character(supplied) && length(supplied) == 1L &&
      nzchar(supplied) && identical(supplied, token)
  }

  # ---- Core app ----
  app <- list(call = function(req) {
    path <- req$PATH_INFO
    method <- req$REQUEST_METHOD

    # ---- GET /ping ----
    if (path == "/ping" && method == "GET") {
      return(list(status = 200L,
                  headers = list("Content-Type" = "text/plain"),
                  body = "pong"))
    }

    if (!is_authorized(req)) {
      return(json_response(
        list(success = FALSE, output = "Missing or invalid X-APRIL-Token"),
        status = 401L
      ))
    }

    # ---- POST /eval ----
    if (path == "/eval" && method == "POST") {
      result <- tryCatch({
        body_raw <- req$rook.input$read(-1)
        body_text <- rawToChar(body_raw)
        parsed <- tryCatch(jsonlite::fromJSON(body_text),
                           error = function(e) NULL)
        if (is.null(parsed) || is.null(parsed$code) ||
            !is.character(parsed$code) || length(parsed$code) != 1L) {
          return(json_response(
            list(success = FALSE,
                 output = "Invalid JSON: 'code' must be one string"),
            status = 400L))
        }
        code <- parsed$code

        # Log + live source sync
        append_to_history(code)
        append_to_source(code)

        # Execute in global environment
        before <- ls(.GlobalEnv, all.names = TRUE)
        out <- capture.output({
          value <- eval(parse(text = code), envir = .GlobalEnv)
        })
        after <- ls(.GlobalEnv, all.names = TRUE)

        # Auto-print plot objects to the Plots pane
        auto_print_plots(value)

        # Naming convention check on newly created variables
        new_vars <- setdiff(after, before)
        naming_warnings <- check_naming(new_vars)

        # Refresh environment guide
        update_env_guide()

        list(success = TRUE,
             output = out,
             new_variables = new_vars,
             naming_warnings = naming_warnings)
      }, error = function(e) {
        list(success = FALSE, output = conditionMessage(e))
      })
      return(json_response(result))
    }

    # ---- GET /objects ----
    if (path == "/objects" && method == "GET") {
      objs <- ls(.GlobalEnv)
      info <- lapply(objs, function(n) {
        o <- get(n, envir = .GlobalEnv)
        entry <- list(name = n)
        desc <- if (exists(n, envir = var_descriptions, inherits = FALSE))
          var_descriptions[[n]] else ""
        if (nchar(desc) > 0) entry$description <- desc
        if (inherits(o, "Seurat")) {
          entry$type <- "Seurat"
          entry$cells <- ncol(o)
          entry$features <- nrow(o)
        } else if (is.data.frame(o)) {
          entry$type <- "data.frame"
          entry$rows <- nrow(o)
          entry$cols <- ncol(o)
        } else if (is.matrix(o)) {
          entry$type <- "matrix"
          entry$rows <- nrow(o)
          entry$cols <- ncol(o)
        } else if (is.list(o)) {
          entry$type <- "list"
          entry$length <- length(o)
        } else if (is.function(o)) {
          entry$type <- "function"
        } else if (is.character(o)) {
          entry$type <- "character"
          entry$length <- length(o)
        } else {
          entry$type <- class(o)[1]
        }
        entry
      })
      return(json_response(info))
    }

    # ---- GET /data/:name ----
    if (grepl("^/data/", path) && method == "GET") {
      obj_name <- sub("^/data/", "", path)
      if (!exists(obj_name, envir = .GlobalEnv)) {
        return(json_response(list(error = paste0("Object '", obj_name,
                                                 "' not found")),
                             status = 404L))
      }
      obj <- get(obj_name, envir = .GlobalEnv)
      result <- tryCatch({
        if (is.data.frame(obj)) {
          n_show <- min(as.integer(max_rows), nrow(obj))
          jsonlite::toJSON(list(name = obj_name, type = "data.frame",
                                rows = nrow(obj), cols = ncol(obj),
                                colnames = colnames(obj),
                                data = obj[1:n_show, , drop = FALSE]),
                           force = TRUE)
        } else if (inherits(obj, "Seurat")) {
          jsonlite::toJSON(list(name = obj_name, type = "Seurat",
                                cells = ncol(obj), features = nrow(obj),
                                assays = names(obj@assays),
                                reductions = names(obj@reductions),
                                meta_cols = colnames(obj[[]])),
                           auto_unbox = TRUE, force = TRUE)
        } else if (is.list(obj)) {
          jsonlite::toJSON(list(name = obj_name, type = "list",
                                length = length(obj), names = names(obj)),
                           auto_unbox = TRUE, force = TRUE)
        } else if (is.vector(obj) && length(obj) <= 100) {
          jsonlite::toJSON(list(name = obj_name, type = class(obj)[1],
                                length = length(obj), value = obj),
                           auto_unbox = TRUE, force = TRUE)
        } else {
          jsonlite::toJSON(list(name = obj_name, type = class(obj)[1],
                                length = length(obj)),
                           auto_unbox = TRUE, force = TRUE)
        }
      }, error = function(e) {
        jsonlite::toJSON(list(error = conditionMessage(e)), auto_unbox = TRUE)
      })
      return(list(status = 200L,
                  headers = list("Content-Type" = "application/json"),
                  body = result))
    }

    # ---- POST /attach ----
    # Optional "description" field keeps the environment guide readable.
    if (path == "/attach" && method == "POST") {
      result <- tryCatch({
        body_raw <- req$rook.input$read(-1)
        body_text <- rawToChar(body_raw)
        parsed <- jsonlite::fromJSON(body_text)
        if (is.null(parsed$name) || is.null(parsed$value)) {
          return(json_response(
            list(success = FALSE, output = "Need 'name' and 'value' fields"),
            status = 400L))
        }
        if (!is.character(parsed$name) || length(parsed$name) != 1L ||
            !grepl("^[a-z][a-z0-9_]{2,}$", parsed$name)) {
          return(json_response(
            list(success = FALSE,
                 output = "'name' must be descriptive lower snake_case"),
            status = 400L))
        }
        assign(parsed$name, parsed$value, envir = .GlobalEnv)
        if (!is.null(parsed$description)) {
          var_descriptions[[parsed$name]] <- parsed$description
        }
        update_env_guide()
        list(success = TRUE,
             output = paste0("Assigned '", parsed$name, "' to .GlobalEnv"))
      }, error = function(e) {
        list(success = FALSE, output = conditionMessage(e))
      })
      return(json_response(result))
    }

    # ---- POST /annotate ----
    # Attach a human-readable description to an existing variable so the
    # environment guide stays meaningful.
    if (path == "/annotate" && method == "POST") {
      result <- tryCatch({
        body_raw <- req$rook.input$read(-1)
        body_text <- rawToChar(body_raw)
        parsed <- jsonlite::fromJSON(body_text)
        if (is.null(parsed$name) || is.null(parsed$description)) {
          return(json_response(
            list(success = FALSE, output = "Need 'name' and 'description' fields"),
            status = 400L))
        }
        if (!exists(parsed$name, envir = .GlobalEnv)) {
          return(json_response(
            list(success = FALSE, output = paste0("'", parsed$name, "' not found")),
            status = 404L))
        }
        var_descriptions[[parsed$name]] <- parsed$description
        update_env_guide()
        list(success = TRUE, output = paste0("Annotated '", parsed$name, "'"))
      }, error = function(e) {
        list(success = FALSE, output = conditionMessage(e))
      })
      return(json_response(result))
    }

    # ---- GET /guide ----
    # Return the environment guide content.
    if (path == "/guide" && method == "GET") {
      if (!file.exists(guide_file)) update_env_guide()
      content <- paste(readLines(guide_file, warn = FALSE), collapse = "\n")
      return(list(status = 200L,
                  headers = list("Content-Type" = "text/plain; charset=utf-8"),
                  body = content))
    }

    # ---- GET /source ----
    # Return the live agent source file.
    if (path == "/source" && method == "GET") {
      if (!file.exists(source_file)) append_to_source("# empty")
      content <- paste(readLines(source_file, warn = FALSE), collapse = "\n")
      return(list(status = 200L,
                  headers = list("Content-Type" = "text/plain; charset=utf-8"),
                  body = content))
    }

    # ---- GET /history ----
    if (path == "/history" && method == "GET") {
      if (!file.exists(history_file)) {
        return(json_response(list(history = "", entries = 0L)))
      }
      lines <- readLines(history_file, warn = FALSE)
      return(json_response(list(file = history_file, lines = length(lines),
                                content = paste(lines, collapse = "\n"))))
    }

    # ---- GET /code ----
    if (path == "/code" && method == "GET") {
      if (!file.exists(history_file)) {
        return(list(status = 200L,
                    headers = list("Content-Type" = "text/plain"),
                    body = "# No code history yet"))
      }
      content <- paste(readLines(history_file, warn = FALSE), collapse = "\n")
      return(list(status = 200L,
                  headers = list("Content-Type" = "text/plain"),
                  body = content))
    }

    list(status = 404L,
         headers = list("Content-Type" = "text/plain"),
         body = paste0("Not found: ", path))
  })

  # ---- Start server ----
  server <- httpuv::startServer(host, as.integer(port), app)

  # Open the live source file in RStudio source pane (if available)
  if (use_rstudio) {
    tryCatch(rstudioapi::documentOpen(source_file),
             error = function(e) NULL)
  }

  if (!quiet) {
    msg <- paste0(
      "\n┌", paste(rep("─", 44), collapse = ""), "┐\n",
      "  APRIL RStudio bridge active\n",
      "  http://", host, ":", port, "\n",
      "\n",
      "  Live code : ", source_file, "\n",
      "  Env guide : ", guide_file, "\n",
      "  Audit log : ", history_file, "\n",
      "└", paste(rep("─", 44), collapse = ""), "┘\n"
    )
    packageStartupMessage(msg)
  }

  bridge <- list(
    server = server,
    host = host,
    port = as.integer(port),
    history_file = history_file,
    source_file = source_file,
    guide_file = guide_file
  )
  class(bridge) <- "april_rstudio_bridge"
  invisible(bridge)
}

#' Stop APRIL's RStudio bridge
#'
#' @param bridge The object returned by april_start_rstudio_bridge().
#' @export
april_stop_rstudio_bridge <- function(bridge) {
  if (!is.null(bridge)) {
    server <- if (inherits(bridge, "april_rstudio_bridge")) {
      bridge$server
    } else {
      bridge
    }
    server$stop()
    message("APRIL RStudio bridge stopped.")
  }
  invisible(NULL)
}
