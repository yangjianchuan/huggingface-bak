FROM node:18
RUN git clone https://github.com/Hk-Gosuto/ChatGPT-Next-Web-LangChain.git
WORKDIR "ChatGPT-Next-Web-LangChain"
ENV NEXT_PUBLIC_ENABLE_NODEJS_PLUGIN=1
RUN yarn install && yarn build

EXPOSE 3000
CMD yarn start