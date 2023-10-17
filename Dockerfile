FROM python:3.11.4-alpine

WORKDIR /todoapp

COPY . .

RUN pip3 install -r requirements.txt

