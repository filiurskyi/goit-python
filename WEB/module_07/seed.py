import datetime
from random import randint, choice

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base, Classes, Grades, Groups, Students, Teachers

DB_URI = "postgresql+psycopg2://postgres:Gh43he5dgfuJKGKhrh45865s845h@localhost/module07"

fake = Faker("en")
# engine = create_engine('sqlite:///mydatabase.db', echo=True)
engine = create_engine(DB_URI,echo=True,)

DBSession = sessionmaker(bind=engine)
session = DBSession()

CLASSES_NAMES = [
    "Astronomy",
    "Physics",
    "Maths",
    "Computer Science",
    "Programming",
    "Philosopy",
    "Biology",
]

GRADES_NAMES = [5, 4, 3, 2, 1]


def generate_students(amount):
    for _ in range(amount):
        grps = session.query(Groups.id).all()
        print("-------------------", grps)
        new_student = Students(
            f_name=fake.first_name(), l_name=fake.last_name(), stud_group=grps
        )
        session.add(new_student)
        session.commit()
        session.close()


def generate_teachers(amount):
    for _ in range(amount):
        new_teacher = Teachers(
            f_name=fake.first_name(),
            l_name=fake.last_name(),
            # classes=session.query(Classes).group_by("id"),
        )
        session.add(new_teacher)
        session.commit()
        session.close()


def generate_classes():
    for cls in CLASSES_NAMES:
        new_class = Classes(
            name=cls,
        )
        session.add(new_class)
        session.commit()
        session.close()


def generate_groups(amount):
    for _ in range(amount):
        new_group = Groups(
            name=fake.country(),
        )
        session.add(new_group)
        session.commit()
        session.close()


def generate_grades(amount_per_student):
    for _ in range(amount_per_student):
        new_grade = Grades(
            grade=choice(GRADES_NAMES),
            date=datetime.datetime.now(),
        )
        session.add(new_grade)
        session.commit()
        session.close()


if __name__ == "__main__":
    generate_groups(5)
    generate_classes()
    generate_students(50)
    generate_teachers(10)
    generate_grades(10)
