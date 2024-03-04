FROM lobehub/lobe-chat
EXPOSE 3210
ENV PORT=3210
ENV ACCESS_CODE=""
USER root
RUN mkdir -p /app/.next/cache
RUN chmod -R 777 /app/.next/cache 
RUN mkdir -p nonexistent 
RUN chmod -R 777 nonexistent
USER nextjs
CMD ["node", "server.js"]
