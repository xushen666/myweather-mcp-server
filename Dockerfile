
FROM python:3.12-slim

WORKDIR /app

# 安装 Python 项目依赖
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# 复制服务代码
COPY server.py http_server.py ./

ENV PYTHONUNBUFFERED=1
ENV PORT=8081

EXPOSE 8081

# 启动 HTTP MCP Server
CMD ["python", "http_server.py"]
