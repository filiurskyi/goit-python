--query1.sql
SELECT ROUND(AVG(g.stud_grade), 2), s.stud_f_name, s.stud_l_name
FROM stu_grades as gd
LEFT JOIN students as s ON g.stud_id = s.id
GROUP BY s.stud_f_name
LIMIT 5;