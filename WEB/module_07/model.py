from sqlalchemy import Column, ForeignKey, Integer, SmallInteger, String, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    f_name = Column(String(250), nullable=False)
    l_name = Column(String(250), nullable=False)
    stud_group = Column(SmallInteger, ForeignKey("groups.id"), nullable=False)


class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    f_name = Column(String(250), nullable=False)
    l_name = Column(String(250), nullable=False)
    classes = relationship("Classes")


class Classes(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    teachers = Column(SmallInteger, ForeignKey("teachers.id"))


class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Grades(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    class_id = Column(SmallInteger, ForeignKey("classes.id"))
    teacher_id = Column(SmallInteger, ForeignKey("teachers.id"))
    date = Column(DateTime)
