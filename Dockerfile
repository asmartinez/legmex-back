FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /django-login
COPY requirements.txt /django-login/
RUN pip3 install -r requirements.txt
COPY . /django-login/