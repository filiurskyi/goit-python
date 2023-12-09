from sqlalchemy import func, select, desc

from model import Grade, Group, Student, Subject, Teacher
from seed import session

from pprint import pprint


def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    query = (
        select(
            Student.f_name,
            Student.l_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.pk)
        .limit(5)
    )
    result = session.execute(query).all()
    print(result)


def select_2():
    # Знайти студента із найвищим середнім балом з певного предмета.
    subquery = (
        session.query(
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            Student.pk.label("student_pk"),  # Alias Student.pk as student_pk
            Grade.subject_pk.label("subject_pk"),  # Include subject_pk in the subquery
        )
        .join(Student, Student.pk == Grade.student_pk)
        .group_by(Grade.student_pk, Grade.subject_pk)
        .subquery()
    )

    query = (
        session.query(
            subquery.c.student_pk,  # Use the correct alias here
            subquery.c.subject_pk,  # Include subject_pk in the result
            Student.pk,  # Include students.pk in the result
            func.max(subquery.c.avg_grade).label(
                "max_avg_grade"
            ),  # Correct the column name here
        )
        .join(
            Student, Student.pk == subquery.c.student_pk
        )  # Join with the Student table
        .group_by(
            subquery.c.student_pk, subquery.c.subject_pk, Student.pk
        )  # Include Student.pk in the GROUP BY clause
        .order_by(desc("max_avg_grade"))
        .limit(5)
    )

    result = session.execute(query).all()
    print(result)


def select_3(subject_pk: int):
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
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    query = session.execute(
        select(func.avg(Grade.grade))
    ).all()
    pprint(query)


def select_5():
    # Знайти які курси читає певний викладач.
    query = session.execute(
        select(Teacher.f_name, Teacher.l_name, Subject.name)
        .join(Subject)
    ).all()
    pprint(query)


def select_6(group_id: int):
    # Знайти список студентів у певній групі.
    query = session.execute(
        select(Student.f_name, Student.l_name, Group.name)
        .join(Group)
        .where(Group.pk == group_id)
    ).all()
    pprint(query)


def select_7(group_id: int, subject_id: int):
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


def select_8():
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    query = session.query(Student.f_name, Student.l_name).limit(2).all()
    print(query)


def select_9():
    # Знайти список курсів, які відвідує певний студент.
    query = session.query(Student.f_name, Student.l_name).limit(2).all()
    print(query)


def select_10():
    # Список курсів, які певному студенту читає певний викладач.
    query = session.query(Student.f_name, Student.l_name).limit(2).all()
    print(query)


if __name__ == "__main__":
    # select_1()
    # select_2()
    # select_3(1)
    # select_4()
    # select_5()
    # select_6(1)
    select_7(1, 1)
    # select_8()
    # select_9()
    # select_10()
