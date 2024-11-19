FROM python:3.13.0

ENV PYTHONUNBUFFERED 1

RUN mkdir /WORKDIR

WORKDIR /WORKDIR

COPY requeriments.txt /WORKDIR/

RUN python -m pip install -r requeriments.txt

COPY . /WORKDIR/