FROM python:3.11-slim
LABEL authors="strixprogrammer"

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . .

VOLUME $APP_HOME/storage

#EXPOSE 3000

ENTRYPOINT ["python", "/app/app.py"]