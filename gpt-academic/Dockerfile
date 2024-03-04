FROM python:3.11

# 安装 git
RUN apt-get update && apt-get install -y git

# 更新 pip
RUN pip install --upgrade pip

# 拉取仓库到 app 文件夹
RUN git clone https://github.com/binary-husky/gpt_academic.git /app

# 将 app 目录设置为当前目录
WORKDIR /app

# 从 requirements.txt 安装依赖
RUN pip install -r requirements.txt

# 创建 gpt_log 目录并设置权限
RUN mkdir gpt_log && chown -R 1000:1000 gpt_log
# 创建 private_upload 目录并设置权限
RUN mkdir private_upload && chown -R 1000:1000 private_upload
# 设置环境变量
ENV WEB_PORT=12345
ENV AUTO_CLEAR_TXT=True
ENV DARK_MODE=False
ENV AUTO_CLEAR_TXT=True
ENV TIMEOUT_SECONDS=60
ENV MAX_RETRY=3
ENV ALLOW_RESET_CONFIG=False
ENV LLM_MODEL=gpt-3.5-turbo
ENV AVAIL_LLM_MODELS='["gpt-3.5-turbo", "gpt-4-turbo-preview"]'

# 开放 端口
EXPOSE 12345

# 启动
CMD ["python3", "-u", "main.py"]