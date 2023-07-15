FROM python:3.11-bullseye

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
WORKDIR /app/cashman
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .