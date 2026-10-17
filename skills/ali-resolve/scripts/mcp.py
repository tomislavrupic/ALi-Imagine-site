#!/usr/bin/env python3
"""Diagnostic access to the installed ALi MCP client; no automatic retry."""
import importlib.util, json, pathlib, sys
path=pathlib.Path.home()/'Library/Application Support/ALi-Imagine/mcp/server.py'
spec=importlib.util.spec_from_file_location('ali_mcp',path)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
if len(sys.argv)!=3: raise SystemExit('Usage: mcp.py ali_tool JSON_arguments')
print(json.dumps(module.call(sys.argv[1],json.loads(sys.argv[2])),indent=2))
