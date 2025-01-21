# 使用官方的Python基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 8000

# 运行Django开发服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]