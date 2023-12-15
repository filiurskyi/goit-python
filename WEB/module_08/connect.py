from os import getenv

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()
DB_USER = getenv("DB_USER")
DB_PW = getenv("DB_PW")
DATABASE = getenv("DATABASE")
URI = f"mongodb+srv://{DB_USER}:{DB_PW}@cluster0.oaihoro.mongodb.net/{DATABASE}?retryWrites=true&w=majority"

client = MongoClient(URI, server_api=ServerApi("1"))
db = client.homework