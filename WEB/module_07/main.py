from sqlalchemy import create_engine
from psycopg2 import connect


engine = create_engine('sqlite:///:memory:', echo=True)
# engine = create_engine('postgres+psycopg2:///:localhost:', echo=True)
