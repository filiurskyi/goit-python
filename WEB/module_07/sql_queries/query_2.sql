--query2.sql Знайти студента із найвищим середнім балом з певного предмета.

SELECT MAX(sq.aver) AS max_avg_grade, sq.student_pk, sq.subject_pk, sq.f_name, sq.l_name
FROM (
    SELECT AVG(gd.grade) as aver, gd.student_pk, gd.subject_pk, s.f_name, s.l_name
    FROM grades AS gd
    LEFT JOIN students AS s ON gd.student_pk = s.pk
    GROUP BY gd.student_pk, gd.subject_pk, s.f_name, s.l_name
) AS sq
GROUP BY sq.student_pk, sq.subject_pk, sq.f_name, sq.l_name;
