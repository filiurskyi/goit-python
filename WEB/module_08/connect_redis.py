import os
import redis

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_USER = os.getenv("REDIS_USER")
REDIS_PW = os.getenv("REDIS_PW")
REDIS_DB = os.getenv("REDIS_DB")

redis_connector = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, username=REDIS_USER, password=REDIS_PW, db=REDIS_DB)


def redis_setter(key: str, val: str, connection: redis.Redis):
    connection.set(key, val)
    print(f"wrote to db {key=}, {val=}")


def redis_getter(key: str, connection: redis.Redis):
    val = connection.get(key)
    return f"got from db {key=}, {val=}"
