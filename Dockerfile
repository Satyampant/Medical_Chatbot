FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN uv sync

CMD ["python3", "app.py"]