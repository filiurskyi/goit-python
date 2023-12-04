--query1.sql - Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT ROUND(AVG(gd.stud_grade), 2), s.stud_f_name, s.stud_l_name
FROM stud_grades as gd
LEFT JOIN students as s ON gd.stud_id = s.id
GROUP BY s.stud_f_name
LIMIT 5;