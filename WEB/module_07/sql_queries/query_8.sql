--query8.sql Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT teachers.f_name, teachers.l_name, avg(grades.grade) AS avg_1, subjects.name
FROM teachers JOIN grades ON teachers.pk = grades.teacher_pk JOIN subjects ON subjects.pk = grades.subject_pk GROUP BY teachers.f_name, teachers.l_name, subjects.name