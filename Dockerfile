FROM arm32v7/python:3.9-bullseye as base-prod

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./pip.conf /etc/pip.conf

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade gunicorn

RUN apt-get update
RUN apt-get install libatlas-base-dev libopenblas-dev -y

COPY ./requirements.txt /app/requirements.txt
RUN python3 -m pip install --no-cache-dir --only-binary=:all: -r requirements.txt

#ENV SCRIPT_NAME=/einkaufs_api

CMD python3 manage.py makemigrations collect && python3 manage.py migrate && gunicorn --bind 0.0.0.0:80 einkaufs_api_rest.wsgi
