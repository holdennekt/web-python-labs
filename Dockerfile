FROM python:3.10.6-slim

ENV FLASK_APP=src

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY src /opt/src

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p 3000