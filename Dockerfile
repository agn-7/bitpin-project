FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV DJANGO_CONFIGURATION Docker

RUN mkdir /code

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    curl \
    htop \
    ipython3 \
    nano \
    iputils-ping

RUN pip install --upgrade pip
RUN pip install --default-timeout=105 future

WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt

COPY . /code
