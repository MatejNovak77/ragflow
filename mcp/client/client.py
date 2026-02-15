#
#  Copyright 2025 The InfiniFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#


from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
import sys

def format_output(response):
    import json
    import sys
    import re

    data = response.model_dump()
    pretty = json.dumps(data, indent=2, ensure_ascii=False)

    # If stdout is not a TTY (e.g. redirected to file), return plain JSON
    if not sys.stdout.isatty():
        return "=== RAGFlow MCP Tool Response ===\n" + pretty

    # Simple ANSI colors for terminal use
    CYAN = "\033[96m"
    GREEN = "\033[92m"  # for all JSON string values (including keys)
    RESET = "\033[0m"

    # Colorize all JSON string tokens (text values) but leave structure ({ } [ ] : ,) uncolored
    string_pattern = r'"([^"\\]|\\.)*"'

    def color_strings(match):
        return f"{GREEN}{match.group(0)}{RESET}"

    colored_body = re.sub(string_pattern, color_strings, pretty)

    return f"{CYAN}=== RAGFlow MCP Tool Response ==={RESET}\n{colored_body}"

def format_tools(tools):
    import json, sys, re
    data = [t.model_dump() for t in tools.tools]
    pretty = json.dumps(data, indent=2, ensure_ascii=False)
    if not sys.stdout.isatty():
        return "=== Available MCP Tools ===\n" + pretty
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    string_pattern = r'"([^"\\]|\\.)*"'
    def color_strings(m):
        return f"{GREEN}{m.group(0)}{RESET}"
    colored = re.sub(string_pattern, color_strings, pretty)
    return f"{CYAN}=== Available MCP Tools ==={RESET}\n{colored}"

async def main():
    # Read question from command line argument
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = ""
    try:
        # To access RAGFlow server in `host` mode, you need to attach `api_key` for each request to indicate identification.
        # async with sse_client("http://localhost:9382/sse", headers={"api_key": "ragflow-IyMGI1ZDhjMTA2ZTExZjBiYTMyMGQ4Zm"}) as streams:
        # Or follow the requirements of OAuth 2.1 Section 5 with Authorization header
        # async with sse_client("http://localhost:9382/sse", headers={"Authorization": "Bearer ragflow-IyMGI1ZDhjMTA2ZTExZjBiYTMyMDQ4Zm"}) as streams:

        async with sse_client(
            "https://rag-dev.byzkids.com:8443/sse",
            headers={"Authorization": "Bearer ragflow-AyZmJmZTBjYWU1MTExZjA4NTRlMDI0Mm"}
        ) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                tools = await session.list_tools()
                print(format_tools(tools))
                response = await session.call_tool(
                    name="ragflow_retrieval",
                    arguments={
                        "dataset_ids": [],
                        "document_ids": [],
                        "question": query
                    }
                )
                print(format_output(response))

    except Exception as e:
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    from anyio import run

    run(main)
