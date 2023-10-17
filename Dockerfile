FROM python:3.11.4-alpine

WORKDIR /todoapp

COPY . .

RUN apt-get update 
RUN pip3 install -r requirements.txt
EXPOSE 8000:8000
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]

