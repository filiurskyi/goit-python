from os import getenv

import mongoengine as me
from dotenv import load_dotenv

load_dotenv()

DB_USER = getenv("DB_USER")
DB_PW = getenv("DB_PW")
DATABASE = getenv("DATABASE")

URI = f"mongodb+srv://{DB_USER}:{DB_PW}@cluster0.oaihoro.mongodb.net/{DATABASE}?retryWrites=true&w=majority"

me.connect(host=URI)


# person_dict = {
#     "fullname": fullname,
#     "born_date": born_date,
#     "born_location": born_location,
#     "description": description,
# }
#
# quote_dict = {
#     "tags": [],
#     "author": author,
#     "quote": quote,
# }
