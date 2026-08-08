# Supervised execution in a live RStudio session

Use this capability only when the user asks APRIL to work in an open RStudio session or when preserving that session's loaded objects is necessary. It is an execution transport, not an analytical method, model-selection criterion, or additional method card.

## Start in RStudio

Install the two required packages explicitly if needed:

```r
install.packages(c("httpuv", "jsonlite"))
```

Set the research project as the working directory, create a temporary secret, source APRIL's integrated script, and start the bridge:

```r
token <- paste(sample(c(letters, LETTERS, 0:9), 48, replace = TRUE), collapse = "")
Sys.setenv(APRIL_RSTUDIO_TOKEN = token)

april_root <- path.expand("~/.codex/skills/APRIL")
source(file.path(april_root, "april-04-analysis", "scripts", "rstudio_bridge.R"))
april_bridge <- april_start_rstudio_bridge()

token  # Give this temporary token to the authorised Codex task only.
```

Do not add this startup to `.Rprofile`. Start it for the bounded analysis session and stop it afterward:

```r
april_stop_rstudio_bridge(april_bridge)
Sys.unsetenv("APRIL_RSTUDIO_TOKEN")
```

## Connect from APRIL

Set the same token in the shell environment used by Codex, without placing it in a repository:

```bash
export APRIL_RSTUDIO_TOKEN='the-temporary-token-from-rstudio'
CLIENT="$HOME/.codex/skills/APRIL/april-04-analysis/scripts/rstudio_bridge_client.py"
python3 "$CLIENT" ping
python3 "$CLIENT" objects
python3 "$CLIENT" guide
```

Use `eval --file analysis_step.R` for multi-line code so shell quoting cannot alter it. Short, auditable expressions may use `eval --code 'summary(analysis_data)'`. Other commands are `data`, `attach`, `annotate`, `source`, `code`, and `history`; run `--help` for their arguments.

## Required interaction sequence

1. Ping the bridge and stop if it is unavailable.
2. Inspect `objects` and `guide` before executing code. Retrieve only the objects or limited rows required for the stated analysis.
3. Confirm the analysis target, substantive method card, object names, variables, and requested outputs. A live session does not relax Stage 04's model-selection rules.
4. Send small, commented, logically complete R blocks. Preserve readable lower `snake_case` names and avoid overwriting user objects unless explicitly authorised.
5. Check `success`, captured output, new variables, naming warnings, and the refreshed object inventory after every evaluation. Diagnose errors before continuing.
6. Annotate important derived objects, models, tables, and figures so `april_environment_guide.md` remains intelligible.
7. Retrieve `code` or `history` and consolidate the accepted steps into the project's reproducible analysis script. The HTTP audit trail is evidence of execution, not the final reproducibility package.
8. Rerun from a clean session when feasible, reconcile objects with tables and prose, then ask the user to stop the bridge.

## Security and scope

- The server is hard-limited to `127.0.0.1` and requires `X-APRIL-Token` for every endpoint except `/ping`. Never weaken either control.
- `/eval` deliberately permits arbitrary R execution with the user's account. Do not install packages, delete or overwrite files/objects, transmit data, expose credentials, or alter persistent startup files unless the user explicitly requests that exact action.
- Treat object names and summaries as potentially sensitive. Do not retrieve full data merely because `/data` is available; its data-frame response is capped, but minimisation still applies.
- Keep the bridge on demand. Stop it when the requested analysis ends, when the user changes tasks, or when supervision is no longer available.
- Preserve the user's requested stopping point. RStudio access authorises execution needed for the requested analysis, not additional models, manuscript sections, or a complete paper.

The integrated R server is adapted from `brucehu-create/rstudio-bridge` under the MIT licence. Provenance and adaptation details are recorded in `sources.md`; the retained licence notice is beside the script.
