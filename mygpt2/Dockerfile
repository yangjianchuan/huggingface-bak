FROM xyhelper/cockroachai:latest
RUN mkdir -p /app/config && chmod 777 /app/config
RUN mkdir -p /app/resource/template && chmod 777 /app/resource/template
ENV OAUTH_URL="http://127.0.0.1:9000/oauth"
# 创建/config目录并写入配置到config.yaml文件
RUN mkdir -p /app/config && \
    echo "cool:" > /app/config/config.yaml && \
    echo "  autoMigrate: true" >> /app/config/config.yaml && \
    echo "database:" >> /app/config/config.yaml && \
    echo "  default:" >> /app/config/config.yaml && \
    echo "    type: \"sqlite\"" >> /app/config/config.yaml && \
    echo "    name: \"./config/cool.sqlite\"" >> /app/config/config.yaml && \
    echo "    extra: busy_timeout=5000" >> /app/config/config.yaml && \
    echo "    createdAt: \"create_time\"" >> /app/config/config.yaml && \
    echo "    updatedAt: \"update_time\"" >> /app/config/config.yaml

# 设置文件权限为777
RUN chmod 777 /app/config/config.yaml
