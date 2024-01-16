FROM debian:bullseye-slim
RUN apt-get update && apt-get install -y curl

RUN version=$(basename $(curl -sL -o /dev/null -w %{url_effective} https://github.com/gngpp/ninja/releases/latest)) \
    && base_url="https://github.com/gngpp/ninja/releases/expanded_assets/$version" \
    && latest_url=https://github.com/$(curl -sL $base_url | grep -oP 'href=".*x86_64.*musl\.tar\.gz(?=")' | sed 's/href="//') \
    && curl -Lo ninja.tar.gz $latest_url \
    && tar -xzf ninja.tar.gz


ENV LANG=C.UTF-8 DEBIAN_FRONTEND=noninteractive LANG=zh_CN.UTF-8 LANGUAGE=zh_CN.UTF-8 LC_ALL=C

RUN cp ninja /bin/ninja
RUN mkdir /.gpt3 && chmod 777 /.gpt3
RUN mkdir /.gpt4 && chmod 777 /.gpt4
RUN mkdir /.auth && chmod 777 /.auth
RUN mkdir /.platform && chmod 777 /.platform

CMD ["/bin/ninja","run"]