FROM python:3.11-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY pyproject.toml poetry.lock .
RUN pip install poetry && poetry install --no-root --no-directory
COPY . .
RUN poetry install
RUN pip install colorama

ENTRYPOINT ["python", "/app/src/main.py"]