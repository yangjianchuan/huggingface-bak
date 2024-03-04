FROM node:18
RUN apt update 
RUN apt install git
RUN git clone https://github.com/Hansimov/llm-mixer.git /app
WORKDIR "/app"
RUN npm install
EXPOSE 23456
CMD node server.js