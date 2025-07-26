FROM python:3.12-slim-buster

WORKDIR /app

COPY . /app

RUN uv sync

CMD ["python3", "app.py"]