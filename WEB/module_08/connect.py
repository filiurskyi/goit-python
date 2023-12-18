from os import getenv

from dotenv import load_dotenv
from mongoengine import connect


load_dotenv()
DB_USER = getenv("DB_USER")
DB_PW = getenv("DB_PW")
DATABASE = getenv("DATABASE")
URI = f"mongodb+srv://{DB_USER}:{DB_PW}@cluster0.oaihoro.mongodb.net/{DATABASE}?retryWrites=true&w=majority"

connect(host=URI, ssl=True)
