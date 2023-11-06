# Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

USER root

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER 10015

CMD ["pytest"]
