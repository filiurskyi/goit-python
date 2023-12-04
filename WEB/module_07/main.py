from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from psycopg2 import connect
from model import Base, Students, Groups, Teachers, Classes, Grades
from faker import Faker

fake = Faker("en")
engine = create_engine('sqlite:///mydatabase.db', echo=True)
# engine = create_engine('postgres+psycopg2:///:localhost:', echo=True)

DBSession = sessionmaker(bind=engine)
session = DBSession()

Base.metadata.create_all(engine)
Base.metadata.bind = engine


for _ in range(10):
    new_student = Students(
        f_name = fake.first_name(),
        l_name = fake.last_name(),
        stud_group = 1,
    )
    session.add(new_student)
    session.commit()
