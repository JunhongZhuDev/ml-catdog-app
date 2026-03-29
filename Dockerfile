# 使用官方 Python 3.9.13 镜像
FROM python:3.9.13-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 升级 pip 并安装依赖
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 复制项目代码
COPY . .

# 暴露 FastAPI 默认端口
EXPOSE 8000

# 启动 FastAPI 应用
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]