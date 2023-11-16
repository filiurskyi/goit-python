FROM python:3.12-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . .

VOLUME $APP_HOME/storage

EXPOSE 3000

ENTRYPOINT ["python", "/app/app.py"]