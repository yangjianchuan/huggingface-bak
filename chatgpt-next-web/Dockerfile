FROM node:18
RUN git clone https://github.com/Yidadaa/ChatGPT-Next-Web.git
WORKDIR "ChatGPT-Next-Web"
RUN npm i 
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "start"]