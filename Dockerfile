FROM python:3
MAINTAINER jdeorio@safaribooksonline.com

ENV DEBIAN_FRONTEND noninteractive

# Install system dependencies
RUN apt-get update -y && \
    apt-get install -y daemontools && \
    rm -rf /var/lib/apt/lists/*

# Create the working directory
RUN mkdir /reallylonglink/
WORKDIR /reallylonglink/

# Install pip libraries
RUN pip install -U pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
