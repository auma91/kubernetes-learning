FROM node:alpine

#Set Envir
ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_DATABASE app
ENV MYSQL_USER app
ENV MYSQL_PASSWORD app
ENV MYSQL_USER_MONITORING monitoring
ENV MYSQL_PASSWORD_MONITORING monitoring

RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                mysql \
                python3-dev \
        ;
RUN pip3 install --upgrade pip
WORKDIR /app
COPY . /app/
RUN pip3 --no-cache-dir install -r requirements.txt
WORKDIR /app/client
RUN npm install



WORKDIR /scripts

WORKDIR /app/backend
CMD ["python3", "mysql1.py"]
WORKDIR /app/client
CMD ["npm" ,"start"]



EXPOSE 3000
EXPOSE 3306
EXPOSE 5000
