import os
from datetime import datetime
from random import randint, random
from sqlite3 import Connection, Cursor

from faker import Faker


def db_filler(cur):
    faker_start_date = datetime.strptime("2022-01-01", "%Y-%m-%d")
    faker_end_date = datetime.strptime("2023-01-01", "%Y-%m-%d")

    fake = Faker()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS stud_groups(id INTEGER PRIMARY KEY, group_name VARCHAR(100));"
    )
    for _ in range(3):
        cur.execute(
            f"INSERT INTO stud_groups (group_name) VALUES ('GR_{fake.street_suffix()}')"
        )
    connection.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT, stud_f_name VARCHAR(100) NOT NULL, stud_l_name VARCHAR(100) NOT NULL, stud_group INTEGER, FOREIGN KEY (stud_group) REFERENCES stud_groups (id) ON DELETE SET NULL ON UPDATE CASCADE);"
    )
    for _ in range(40):
        cur.execute(
            f"INSERT INTO students (stud_f_name, stud_l_name, stud_group) VALUES ('{fake.first_name()}', '{fake.last_name()}', {randint(1, 3)})"
        )
    connection.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS classes(id INTEGER PRIMARY KEY, class_name VARCHAR(100));"
    )
    for i in range(len(classes_names)):
        cur.execute(f"INSERT INTO classes (class_name) VALUES ('{classes_names[i]}')")
    connection.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS teachers(id INTEGER PRIMARY KEY, teacher_f_name VARCHAR(100), teacher_l_name VARCHAR(100), teacher_class INTEGER, FOREIGN KEY (teacher_class) REFERENCES classes (id) ON DELETE SET NULL ON UPDATE CASCADE);"
    )
    for _ in range(10):
        cur.execute(
            f"INSERT INTO teachers (teacher_f_name, teacher_l_name, teacher_class) VALUES ('{fake.first_name()}', '{fake.last_name()}', '{randint(1, len(classes_names)+1)}')"
        )
    connection.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS stud_grades(id INTEGER PRIMARY KEY, stud_id INTEGER, stud_grade VARCHAR(1), grade_date DATE, grade_on_class INTEGER, FOREIGN KEY (grade_on_class) REFERENCES classes (id) ON DELETE SET NULL ON UPDATE CASCADE, FOREIGN KEY (stud_id) REFERENCES students (id) ON DELETE SET NULL ON UPDATE CASCADE);"
    )
    students_id_list = cur.execute("SELECT id FROM students;").fetchall()
    for student_id in students_id_list:
        for _ in range(randint(10, 20)):
            query = f"INSERT INTO stud_grades (stud_id, stud_grade, grade_date, grade_on_class) VALUES ({student_id[0]}, '{grades_names[randint(0, len(grades_names)-1)]}', '{fake.date_between(start_date=faker_start_date, end_date=faker_end_date)}','{randint(1, len(classes_names)+1)}');"
            cur.execute(query)

    connection.commit()


def write_empty_sql_files():
    for i in range(1, 11):
        with open(f"query_{i}.sql" ,"w") as f:
            f.write(f"--query{i}.sql\nSELECT * FROM students")


def rewrite_db():
    try:
        os.remove("db.sqlite3")
        print("old file deleted")
        db_filler(cursor)
    except FileNotFoundError:
        print("old file not found")
    except PermissionError:
        print("Perssion Error. Using old DB")


if __name__ == "__main__":
    classes_names = [
        "Astronomy",
        "Physics",
        "Maths",
        "Computer Science",
        "Programming",
        "Philosopy",
        "Biology",
    ]
    grades_names = [
        "5",
        "4",
        "3",
        "2",
        "1",
    ]


    database = "db.sqlite3"
    connection = Connection(database)
    cursor = Cursor(connection)
    # db_filler(cursor)

    for i in range(1, 11):
        with open(f"query_{i}.sql" ,"r") as f:
            query = f.read()
            print(query)
            print(cursor.execute(query).fetchall())



    connection.close()
