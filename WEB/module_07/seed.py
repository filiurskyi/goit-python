import datetime
from random import choice, randint

from faker import Faker
from model import Base, Grade, Group, Student, Subject, Teacher
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URI = (
    "postgresql+psycopg2://postgres:Gh43he5dgfuJKGKhrh45865s845h@localhost/module07"
)

fake = Faker("en")
engine = create_engine(
    DB_URI,
    echo=True,
)

DBSession = sessionmaker(bind=engine)
session = DBSession()

SUBJECTS_NAMES = [
    "Astronomy",
    "Physics",
    "Maths",
    "Computer Science",
    "Programming",
    "Philosophy",
    "Biology",
]

GRADES_NAMES = [5, 4, 3, 2, 1]


def generate_students(amount):
    for _ in range(amount):
        grps = session.query(Group.pk).all()
        new_student = Student(
            f_name=fake.first_name(),
            l_name=fake.last_name(),
            stud_group=choice(grps)[0],
        )
        session.add(new_student)
        session.commit()
    session.close()


def generate_teachers(amount):
    for _ in range(amount):
        cls = session.query(Subject.pk).all()
        print("--------------", choice(cls)[0])
        new_teacher = Teacher(
            f_name=fake.first_name(),
            l_name=fake.last_name(),
            subject=choice(cls)[0],
        )
        session.add(new_teacher)
        session.commit()
    session.close()


def generate_subjects():
    for sbj in SUBJECTS_NAMES:
        new_subject = Subject(
            name=sbj,
        )
        session.add(new_subject)
        session.commit()
    session.close()


def generate_groups(amount):
    for _ in range(amount):
        new_group = Group(
            name=fake.country(),
        )
        session.add(new_group)
        session.commit()
    session.close()


def generate_grades(amount_per_student):
    query = session.query(Teacher.pk, Teacher.subject).all()
    students_query = session.query(Student.pk).all()
    for student_pk in students_query:
        for _ in range(amount_per_student):
            teach, subj = choice(query)
            print("===============")
            print(teach)
            print(subj)
            print("===============")
            new_grade = Grade(
                grade=choice(GRADES_NAMES),
                date=datetime.datetime.now(),
                student_pk=student_pk[0],
                subject_pk=subj,
                teacher_pk=teach,
            )
            session.add(new_grade)
            session.commit()
    session.close()


if __name__ == "__main__":
    generate_groups(5)
    generate_subjects()
    generate_students(50)
    generate_teachers(10)
    generate_grades(10)
