FROM node:20
RUN git clone https://github.com/weaigc/bingo.git
WORKDIR "bg"
RUN mkdir -p /bg/.next/cache/images
RUN chmod -R 755 /bg/.next/cache/images
RUN npm i 
RUN npm run build
ENV PORT 7860
EXPOSE 7860
CMD ["npm", "run", "start"]