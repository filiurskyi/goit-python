from random import randint

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base, Classes, Grades, Groups, Students, Teachers

fake = Faker("en")
# engine = create_engine('sqlite:///mydatabase.db', echo=True)
engine = create_engine(
    "postgresql+psycopg2://postgres:Gh43he5dgfuJKGKhrh45865s845h@localhost/module07",
    echo=True,
)

DBSession = sessionmaker(bind=engine)
session = DBSession()

Base.metadata.create_all(engine)
Base.metadata.bind = engine

if __name__ == "__main__":
    for _ in range(10):
        new_student = Students(
            f_name=fake.first_name(),
            l_name=fake.last_name(),
            stud_group=randint(1, 3),
        )
        session.add(new_student)
        session.commit()
