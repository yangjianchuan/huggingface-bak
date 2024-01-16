FROM node:20
RUN git clone https://github.com/weaigc/bingo.git
WORKDIR "bingo"
RUN npm i 
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "start"]