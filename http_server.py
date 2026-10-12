
import os

from fastmcp import FastMCP

# 直接复用之前写好的业务函数
from server import (
    get_server_info,
    get_weather,
    list_supported_cities,
)

# 创建 HTTP 版本的 MCP Server
mcp = FastMCP("weather-http-server")

# 注册三个现有工具
mcp.tool()(get_weather)
mcp.tool()(list_supported_cities)
mcp.tool()(get_server_info)

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8081")),
    )
