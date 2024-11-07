
FROM python:3.12-slim

ARG PORT
ARG HOST

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY main.py main.py
COPY . .

CMD fastapi run main.py --port ${PORT:-8000} --host ${HOST:-0.0.0.0}
