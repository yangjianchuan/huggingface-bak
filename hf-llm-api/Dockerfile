FROM python:3.11
RUN apt update 
RUN apt install git
RUN git clone https://github.com/Hansimov/hf-llm-api.git /app
WORKDIR "/app"
RUN pip install -r requirements.txt
# RUN mkdir -p /data && chmod -R 755 /data
# VOLUME /data
EXPOSE 23333
CMD ["python", "-m", "apis.chat_api"]