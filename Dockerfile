# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set work directory. 
WORKDIR /django-0-hello

# Install dependencies
COPY Pipfile.lock /django-0-hello/

RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /django-0-hello/