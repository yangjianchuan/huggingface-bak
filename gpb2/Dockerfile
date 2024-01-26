# Build Stage
# 使用 golang:alpine 作为构建阶段的基础镜像
FROM golang:alpine AS builder

# 添加 git，以便之后能从GitHub克隆项目
RUN apk --no-cache add git

# 从 GitHub 克隆 go-proxy-bingai 项目到 /workspace/app 目录下
RUN git clone https://github.com/renqabs/gopb.git /workspace/app

# 设置工作目录为之前克隆的项目目录
WORKDIR /workspace/app

# 编译 go 项目。-ldflags="-s -w" 是为了减少编译后的二进制大小
RUN go build -ldflags="-s -w" -tags netgo -trimpath -o go-proxy-bingai main.go

# Runtime Stage
# 使用轻量级的 alpine 镜像作为运行时的基础镜像
FROM alpine

# 设置工作目录
WORKDIR /workspace/app

# 从构建阶段复制编译后的二进制文件到运行时镜像中
COPY --from=builder /workspace/app/go-proxy-bingai .

# 设置环境变量——Cookies"_U"，此处为随机字符
ENV Go_Proxy_BingAI_USER_TOKEN_1="kJs81422hD92467569ncMz9pLaoQWYtX5rG6bE3fZ4iO"

# 暴露8080端口
EXPOSE 8080

# 容器启动时运行的命令
CMD ["/workspace/app/go-proxy-bingai"]