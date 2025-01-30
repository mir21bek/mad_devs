FROM ubuntu:latest
LABEL authors="msuranchiev"

WORKDIR /app

COPY req.txt

RUN pip install --no-cache-dir -r req.txt

COPY . /app
