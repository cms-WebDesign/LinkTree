# Pull base image
FROM python:3
ENV PYTHONUNBUFFERED 1

# Setup linkages to code repositories and add to image

RUN mkdir /code
WORKDIR /code

#Python packages
RUN pip install Django
RUN pip install djangorestframework==3.6.3
RUN pip install markdown
RUN pip install django-filter==1.1
RUN pip install psycopg2-binary
RUN pip install requests
RUN pip install gunicorn==19.6.0

COPY ./code /code
