FROM python:3.11.4-alpine

WORKDIR todoapp/

COPY . .

RUN pip3 install -r requirements.txt
EXPOSE 8000:8000
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]

