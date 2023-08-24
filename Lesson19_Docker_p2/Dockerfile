FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y nginx curl && \
    mkdir -p /data/images/ && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#WORKDIR /app/static/

COPY nginx.conf /etc/nginx/nginx.conf

COPY ./data/images/ /data/images/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;","-c", "/etc/nginx/nginx.conf"]
