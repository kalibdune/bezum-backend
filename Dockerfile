FROM python:3.12-slim
LABEL authors="kalibdune"

RUN pip install poetry

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock alembic.ini /app/

RUN poetry install --only main --no-root

COPY ./bezum /app/bezum

WORKDIR /app
