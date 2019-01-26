FROM python:latest

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

ENV PRACTICEIT_UNAME rasmussenj@bsd405.org
ENV PRACTICEIT_PW P5a7m121bsd

VOLUME /app


