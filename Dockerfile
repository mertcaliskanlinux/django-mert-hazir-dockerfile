FROM python:3.8.5-alpine

RUN apk update && apk add mariadb-dev build-base

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./django_project /app

WORKDIR /app
RUN mkdir -p /home/mertlinux/Desktop/django-docker-compose/django_project/static

COPY ./mysql-config/my.cnf /etc/mysql/my.cnf


COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]
