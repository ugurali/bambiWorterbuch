# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy project
COPY . /code/