from pprint import pprint

from model import Grade, Group, Student, Subject, Teacher
from seed import session
from sqlalchemy import desc, func, select


def select_1():
    print("=============1================")
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    average_grade = func.avg(Grade.grade).label("average_grade")

    query = session.execute(
        select(
            Student.f_name,
            Student.l_name,
            average_grade,
        )
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .group_by(Student.f_name, Student.l_name)
        .order_by(average_grade.desc())
        .limit(5)
    ).all()
    pprint(query)


def select_2(subject_id: int):
    print("=============2================")
    # Знайти студента із найвищим середнім балом з певного предмета.
    average_grade = func.avg(Grade.grade).label("average_grade")

    query = session.execute(
        select(
            Student.f_name,
            Student.l_name,
            Subject.name,
            average_grade,
        )
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .where(Subject.pk == subject_id)
        .group_by(Student.f_name, Student.l_name, Subject.name)
        .order_by(average_grade.desc())
        .limit(5)
    ).all()
    pprint(query)


def select_3(subject_pk: int):
    print("==============3===============")
    # Alchemy 1.x
    # query = (
    #     session.query(func.avg(Grade.grade), Grade.subject_pk, Student.stud_group)
    #     .select_from(Grade)
    #     .join(Student, Student.pk == Grade.student_pk)
    #     .group_by(Student.stud_group, Grade.subject_pk)
    # )
    # result = session.execute(query).all()
    # pprint(result)

    # Alchemy 2.x
    query = session.execute(
        select(func.avg(Grade.grade), Grade.subject_pk, Student.stud_group)
        .select_from(Grade)
        .join(Student)
        .group_by(Student.stud_group, Grade.subject_pk)
        .where(Grade.subject_pk == subject_pk)
    ).all()
    pprint(query)


def select_4():
    print("============4=================")
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    query = session.execute(select(func.avg(Grade.grade))).all()
    pprint(query)


def select_5():
    print("=============5================")
    # Знайти які курси читає певний викладач.
    query = session.execute(
        select(Teacher.f_name, Teacher.l_name, Subject.name).join(Subject)
    ).all()
    pprint(query)


def select_6(group_id: int):
    print("============6=================")
    # Знайти список студентів у певній групі.
    query = session.execute(
        select(Student.f_name, Student.l_name, Group.name)
        .join(Group)
        .where(Group.pk == group_id)
    ).all()
    pprint(query)


def select_7(group_id: int, subject_id: int):
    print("=============7================")
    # Знайти оцінки студентів у окремій групі з певного предмета.
    query = session.execute(
        select(Student.f_name, Student.l_name, Group.name, Subject.name, Grade.grade)
        .join(Group)
        .join(Grade)
        .join(Subject)
        .where(Group.pk == group_id)
        .where(Subject.pk == subject_id)
    ).all()
    pprint(query)


def select_8(teacher_id: int):
    print("=============8================")
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    query = session.execute(
        select(Teacher.f_name, Teacher.l_name, func.avg(Grade.grade), Subject.name)
        .select_from(Teacher)
        .join(Subject)
        .join(Grade)
        .where(Teacher.pk == teacher_id)
        .group_by(Teacher.f_name, Teacher.l_name, Subject.name)
    ).all()
    pprint(query)


def select_9(student_id: int):
    print("============9=================")
    # Знайти список курсів, які відвідує певний студент.
    query = session.execute(
        select(Student.f_name, Student.l_name, Subject.name)
        .select_from(Student)
        .where(Student.pk == student_id)
    ).all()
    pprint(query)


def select_10(teacher_id: int, student_id: int):
    print("==============10===============")
    # Список курсів, які певному студенту читає певний викладач.
    query = session.execute(
        select(
            Student.f_name, Student.l_name, Teacher.f_name, Teacher.l_name, Subject.name
        )
        .select_from(Teacher)
        .join(Subject)
        .where(Teacher.pk == teacher_id)
        .where(Student.pk == student_id)
        .group_by(
            Subject.name, Student.f_name, Student.l_name, Teacher.f_name, Teacher.l_name
        )
    ).all()
    pprint(query)


if __name__ == "__main__":
    select_1()
    # select_2(1)
    # select_3(1)
    # select_4()
    # select_5()
    # select_6(1)
    # select_7(1, 1)
    # select_8(1)
    # select_9(1)
    # select_10(4 ,1)
