from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    pk = Column(Integer, primary_key=True)
    f_name = Column(String(250), nullable=False)
    l_name = Column(String(250), nullable=False)
    stud_group = Column(SmallInteger, ForeignKey("groups.pk"), nullable=False)


class Teacher(Base):
    __tablename__ = "teachers"
    pk = Column(Integer, primary_key=True)
    f_name = Column(String(250), nullable=False)
    l_name = Column(String(250), nullable=False)
    subject = Column(SmallInteger, ForeignKey("subjects.pk"))


class Subject(Base):
    __tablename__ = "subjects"
    pk = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Group(Base):
    __tablename__ = "groups"
    pk = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Grade(Base):
    __tablename__ = "grades"
    pk = Column(Integer, primary_key=True)
    grade = Column(Integer)
    student_pk = Column(SmallInteger, ForeignKey("students.pk"))
    subject_pk = Column(SmallInteger, ForeignKey("subjects.pk"))
    teacher_pk = Column(SmallInteger, ForeignKey("teachers.pk"))
    date = Column(DateTime)
