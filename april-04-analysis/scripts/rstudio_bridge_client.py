#!/usr/bin/env python3
"""Command-line client for APRIL's authenticated local RStudio bridge."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_URL = "http://127.0.0.1:8765"


class BridgeError(RuntimeError):
    """Raised when the bridge cannot complete a request."""


def _request(
    base_url: str,
    path: str,
    *,
    token: str,
    timeout: float,
    payload: dict[str, Any] | None = None,
) -> Any:
    url = f"{base_url.rstrip('/')}{path}"
    headers = {"Accept": "application/json, text/plain"}
    data = None
    method = "GET"

    if path != "/ping":
        if len(token) < 16:
            raise BridgeError(
                "Set APRIL_RSTUDIO_TOKEN to the secret used in RStudio."
            )
        headers["X-APRIL-Token"] = token

    if payload is not None:
        method = "POST"
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    request = urllib.request.Request(
        url, data=data, headers=headers, method=method
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            content_type = response.headers.get("Content-Type", "")
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        raise BridgeError(f"HTTP {exc.code}: {raw}") from exc
    except urllib.error.URLError as exc:
        raise BridgeError(f"Bridge connection failed: {exc.reason}") from exc

    if "application/json" in content_type:
        return json.loads(raw)
    return raw


def _load_json(value: str | None, path: str | None) -> Any:
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    if value is None:
        raise BridgeError("Provide --json or --json-file.")
    return json.loads(value)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Interact with APRIL's supervised local RStudio session."
    )
    parser.add_argument(
        "--url",
        default=os.environ.get("APRIL_RSTUDIO_URL", DEFAULT_URL),
        help=f"Bridge base URL (default: {DEFAULT_URL})",
    )
    parser.add_argument("--timeout", type=float, default=30.0)
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("ping", "objects", "guide", "source", "code", "history"):
        subparsers.add_parser(command)

    data_parser = subparsers.add_parser("data")
    data_parser.add_argument("name")

    eval_parser = subparsers.add_parser("eval")
    eval_source = eval_parser.add_mutually_exclusive_group(required=True)
    eval_source.add_argument("--code")
    eval_source.add_argument("--file")

    attach_parser = subparsers.add_parser("attach")
    attach_parser.add_argument("name")
    attach_source = attach_parser.add_mutually_exclusive_group(required=True)
    attach_source.add_argument("--json")
    attach_source.add_argument("--json-file")
    attach_parser.add_argument("--description")

    annotate_parser = subparsers.add_parser("annotate")
    annotate_parser.add_argument("name")
    annotate_parser.add_argument("description")

    return parser


def _path_and_payload(args: argparse.Namespace) -> tuple[str, dict[str, Any] | None]:
    if args.command in {"ping", "objects", "guide", "source", "code", "history"}:
        return f"/{args.command}", None
    if args.command == "data":
        return f"/data/{urllib.parse.quote(args.name, safe='')}", None
    if args.command == "eval":
        code = args.code
        if args.file:
            code = Path(args.file).read_text(encoding="utf-8")
        return "/eval", {"code": code}
    if args.command == "attach":
        payload = {
            "name": args.name,
            "value": _load_json(args.json, args.json_file),
        }
        if args.description:
            payload["description"] = args.description
        return "/attach", payload
    if args.command == "annotate":
        return "/annotate", {
            "name": args.name,
            "description": args.description,
        }
    raise BridgeError(f"Unsupported command: {args.command}")


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()
    token = os.environ.get("APRIL_RSTUDIO_TOKEN", "")

    try:
        path, payload = _path_and_payload(args)
        result = _request(
            args.url,
            path,
            token=token,
            timeout=args.timeout,
            payload=payload,
        )
    except (BridgeError, OSError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if isinstance(result, (dict, list)):
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if isinstance(result, dict) and result.get("success") is False:
            return 1
    else:
        print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
