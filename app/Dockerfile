FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY flask/ app/

RUN rm -rf /app/static

ENTRYPOINT python3 /app/app.py

