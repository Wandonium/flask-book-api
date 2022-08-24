### First stage
FROM python:slim

WORKDIR /home/flask-book-api

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY . .
RUN chmod +x boot.sh

EXPOSE 5000
ENTRYPOINT [ "./boot.sh" ]

