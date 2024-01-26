FROM xyhelper/cockroachai:latest
RUN mkdir -p /app/config && chmod 777 /app/config
RUN mkdir -p /app/resource/template && chmod 777 /app/resource/template

# 获取config.yaml
RUN --mount=type=secret,id=CONFIG_YAML,mode=0444,required=true \
    cat /run/secrets/CONFIG_YAML > /app/config/config.yaml && chmod 777 /app/config/config.yaml
