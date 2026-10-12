
# Weather MCP Server

基于 HelloAgents 开发的天气查询 MCP Server。

## Features

- 查询城市实时天气
- 查看支持的城市
- 获取服务器信息
- 支持 MCP Stdio 传输

## Tools

| Tool | Description |
|---|---|
| get_weather | 查询指定城市天气 |
| list_supported_cities | 查看支持的城市 |
| get_server_info | 获取服务器信息 |

## Installation

```bash
pip install -r requirements.txt
```

## Usage

本项目使用 MCP Stdio 传输，通常由 MCP Client 启动。

```bash
python client.py
```

## Weather Data Source

https://wttr.in/
