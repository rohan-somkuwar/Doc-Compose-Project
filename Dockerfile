FROM python:alpine

WORKDIR /app

COPY . /app

RUN  pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT FLASK_APP=/app/flaskapp.py flask run --host=0.0.0.0 --port=8000
