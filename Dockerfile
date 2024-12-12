
FROM python:3.12-slim

ARG PORT
ARG HOST

WORKDIR /code

COPY pyproject.toml pyproject.toml
RUN pip install .

COPY main.py main.py
COPY src src/

CMD fastapi run main.py --port ${PORT:-8000} --host ${HOST:-0.0.0.0}
