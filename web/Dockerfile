# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements* /code/
RUN pip install -r requirements_base.txt
RUN pip install -r requirements_extra.txt
COPY . /code/

#RUN mkdir -p /code/eproject/eapp
#RUN django-admin startproject eproject .
#WORKDIR /code/eproject

#RUN django-admin.py startapp eapp /code/eproject/eapp
#RUN django-admin startapp eapp
