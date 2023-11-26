FROM python:3.11-slim
LABEL authors="strixprogrammer"

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#VOLUME $APP_HOME/storage

EXPOSE 3000

WORKDIR $APP_HOME/app

ENTRYPOINT ["python", "sockserver.py"]
#ENTRYPOINT ["python", "webserver.py"]
