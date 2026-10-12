
import json
from datetime import datetime
from typing import Any, Dict

import requests
from hello_agents.protocols import MCPServer

# =========================
# 1. 创建 MCP Server
# =========================

server = MCPServer(
    name="weather-server",
    description="真实天气查询服务"
)


# =========================
# 2. 中文城市名称映射
# =========================

CITY_MAP = {
    "北京": "Beijing",
    "上海": "Shanghai",
    "广州": "Guangzhou",
    "深圳": "Shenzhen",
    "杭州": "Hangzhou",
    "成都": "Chengdu",
    "重庆": "Chongqing",
    "武汉": "Wuhan",
    "西安": "Xi'an",
    "南京": "Nanjing",
    "天津": "Tianjin",
    "苏州": "Suzhou"
}


# =========================
# 3. 获取真实天气数据
# =========================

def get_weather_data(city: str) -> Dict[str, Any]:
    """从 wttr.in 获取天气数据"""

    # 将中文城市名称转换为英文
    city_en = CITY_MAP.get(city, city)

    # 构造天气 API 地址
    url = f"https://wttr.in/{city_en}?format=j1"

    # 发送 HTTP GET 请求
    response = requests.get(
        url,
        timeout=10
    )

    # HTTP 状态码为错误时抛出异常
    response.raise_for_status()

    # 将 JSON 响应解析为 Python 字典
    data = response.json()

    # 提取当前天气
    current = data["current_condition"][0]

    return {
        "city": city,
        "temperature": float(current["temp_C"]),
        "feels_like": float(current["FeelsLikeC"]),
        "humidity": int(current["humidity"]),
        "condition": current["weatherDesc"][0]["value"],
        "wind_speed": round(
            float(current["windspeedKmph"]) / 3.6, 1
        ),
        "visibility": float(current["visibility"]),
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }


# =========================
# 4. 定义 MCP Tools
# =========================

def get_weather(city: str) -> str:
    """获取指定城市的当前天气"""

    try:
        weather_data = get_weather_data(city)

        return json.dumps(
            weather_data,
            ensure_ascii=False,
            indent=2
        )

    except Exception as e:
        return json.dumps(
            {
                "error": str(e),
                "city": city
            },
            ensure_ascii=False
        )


def list_supported_cities() -> str:
    """列出所有支持的中文城市"""

    result = {
        "cities": list(CITY_MAP.keys()),
        "count": len(CITY_MAP)
    }

    return json.dumps(
        result,
        ensure_ascii=False,
        indent=2
    )


def get_server_info() -> str:
    """获取服务器信息"""

    info = {
        "name": "Weather MCP Server",
        "version": "1.0.0",
        "tools": [
            "get_weather",
            "list_supported_cities",
            "get_server_info"
        ]
    }

    return json.dumps(
        info,
        ensure_ascii=False,
        indent=2
    )


# =========================
# 5. 注册 MCP Tools
# =========================

server.add_tool(get_weather)
server.add_tool(list_supported_cities)
server.add_tool(get_server_info)


# =========================
# 6. 启动 MCP Server
# =========================

if __name__ == "__main__":
    server.run()
