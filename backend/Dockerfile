FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_quiz
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip3 install django-cors-headers
RUN pip3 install djangorestframework
RUN pip3 install requests
RUN pip3 install Pillow
RUN pip3 install -r requirements.txt
COPY . /backend/
