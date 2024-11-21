FROM python:3.12.4-alpine3.20
LABEL maintainer="bileichuk.ivan@gmail.com"

ENV PYTHONBUFFERED=1
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .