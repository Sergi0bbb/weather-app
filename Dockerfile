FROM python:3.11.1

RUN mkdir -p /usr/src/weather-app/
WORKDIR /usr/src/weather-app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . /usr/src/weather-app/
RUN pip install --no-cache-dir -r requirements.txt

