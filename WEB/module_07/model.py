from sqlalchemy import Column, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    f_name = Column(String(250), nullable=False)
    l_name = Column(String(250), nullable=False)
    stud_group = Column(SmallInteger)


class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    f_name = Column(String(250), nullable=False)
    l_name = Column(String(250), nullable=False)
    classes = relationship()


class Classes(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    teachers = relationship("Teachers")


class Grades(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)