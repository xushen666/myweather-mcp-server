
import asyncio
import sys
from pathlib import Path

from hello_agents.protocols import MCPClient


async def main():

    # 找到同目录下的 MCP Server
    server_path = Path(__file__).with_name("server.py")

    client = MCPClient([
        sys.executable,
        str(server_path)
    ])

    async with client:

        # =========================
        # 1. 发现工具
        # =========================

        tools = await client.list_tools()

        print("\n=== 可用工具 ===")

        for tool in tools:
            print(tool["name"])

        # =========================
        # 2. 查询广州天气
        # =========================

        print("\n=== 广州天气 ===")

        result = await client.call_tool(
            "get_weather",
            {"city": "广州"}
        )

        print(result)

        # =========================
        # 3. 查询北京天气
        # =========================

        print("\n=== 北京天气 ===")

        result = await client.call_tool(
            "get_weather",
            {"city": "北京"}
        )

        print(result)


if __name__ == "__main__":
    asyncio.run(main())
