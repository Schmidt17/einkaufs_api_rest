FROM arm32v7/python:3.9-bullseye as base-prod

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./pip.conf /etc/pip.conf

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade gunicorn

COPY ./requirements.txt /app/requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade -r requirements.txt

ENV SCRIPT_NAME=/einkaufs_api

CMD python3 manage.py migrate && gunicorn --bind 0.0.0.0:80 einkaufs_api_rest.wsgi