FROM python:3.7-slim-buster

RUN pip install --upgrade pip

# Install requirements
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app