# base image
FROM python:3

# The environment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1

#directory to store app source code
RUN mkdir /app

#switch to /app directory so that everything runs from here
WORKDIR /app

#copy the app code to image working directory
COPY ./app /app

#let pip install required packages
RUN pip install Django
RUN pip install djangorestframework==3.6.3
RUN pip install markdown
RUN pip install django-filter==1.1
RUN pip install psycopg2-binary
RUN pip install requests
RUN pip install gunicorn==19.6.0
RUN pip install django-jquery
