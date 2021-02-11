FROM python:3.9.0-slim

ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
