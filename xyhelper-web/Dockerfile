FROM xyhelper/xyhelper-web:latest
WORKDIR /app
RUN mkdir -p data/sessions  && chmod 777 data/sessions

EXPOSE 8080
CMD ["/bin/sh", "-c" ,"./main"]