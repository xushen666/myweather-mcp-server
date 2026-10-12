
import asyncio

from fastmcp import Client


async def main():
    client = Client("http://127.0.0.1:8081/mcp")

    async with client:
        tools = await client.list_tools()

        print("=== 可用工具 ===")
        for tool in tools:
            print(tool.name)

        result = await client.call_tool(
            "list_supported_cities",
            {}
        )

        print("\n=== 工具调用结果 ===")
        print(result)
        result = await client.call_tool("get_weather", {"city": "广州"})

        print("\n=== 实时天气 ===")
        print(result.data)

if __name__ == "__main__":
    asyncio.run(main())
