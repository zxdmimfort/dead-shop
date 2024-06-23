FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY ./docker/nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]