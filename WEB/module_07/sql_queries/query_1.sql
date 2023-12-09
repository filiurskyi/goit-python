SELECT ROUND(AVG(gd.grade), 2), s.f_name ,s.l_name
FROM grades as gd
LEFT JOIN students as s ON gd.student_pk  = s.pk
GROUP BY s.pk
LIMIT 5;