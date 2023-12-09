from sqlalchemy import func, select, desc

from model import Grade, Group, Student, Subject, Teacher
from seed import session

from pprint import pprint

def select_1():
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


def select_3():
    query = (
        session.query(func.avg(Grade.grade), Grade.subject_pk, Student.stud_group)
        .select_from(Grade)
        .join(Student, Student.pk == Grade.student_pk)
        .group_by(Student.stud_group, Grade.subject_pk)
    )
    result = session.execute(query).all()
    pprint(result)


def select_4():
    query = session.query(Student.f_name, Student.l_name).limit(2).all()
    print(query)


def select_5():
    query = session.query(Student.f_name, Student.l_name).limit(2).all()
    print(query)


def select_6():
    query = session.query(Student.f_name, Student.l_name).limit(2).all()
    print(query)


def select_7():
    query = session.query(Student.f_name, Student.l_name).limit(2).all()
    print(query)


def select_8():
    query = session.query(Student.f_name, Student.l_name).limit(2).all()
    print(query)


def select_9():
    query = session.query(Student.f_name, Student.l_name).limit(2).all()
    print(query)


def select_10():
    query = session.query(Student.f_name, Student.l_name).limit(2).all()
    print(query)


if __name__ == "__main__":
    # select_1()
    # select_2()
    select_3()
    # select_4()
    # select_5()
    # select_6()
    # select_7()
    # select_8()
    # select_9()
    # select_10()
