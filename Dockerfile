# Dockerfile

# pull the official docker image
FROM python:3.9.4-slim

# Create app user to be used by the application
RUN useradd -ms /bin/bash app
WORKDIR /home/app
USER app
MAINTAINER Powered By People


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/home/app/.local/bin:${PATH}"

# Install deps
COPY requirements/base.txt /home/app/
COPY requirements/production.txt /home/app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r production.txt

# Copy the code to the necessary path
COPY . /home/app/

# run entrypoint.prod.sh
ENTRYPOINT ["bash", "docker-entrypoint.sh"]
