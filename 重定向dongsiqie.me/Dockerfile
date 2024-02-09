# 使用官方的Python基础镜像
FROM python:3.8-slim

# 设置工作目录，之后的命令都会在这个目录下执行
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录下
COPY . /app

# 安装Flask库
RUN pip install Flask

# 告诉Docker在运行容器时监听的端口号
EXPOSE 5000

# 设置环境变量，确保Flask运行在生产模式
ENV FLASK_ENV=development

# 设置启动命令，运行Flask应用
CMD ["flask", "run", "--host=0.0.0.0"]
