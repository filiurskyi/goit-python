--query2.sql Знайти студента із найвищим середнім балом з певного предмета.

SELECT MAX(sq.aver) AS max_avg_grade, sq.stud_id, sq.grade_on_class, sq.stud_f_name, sq.stud_l_name
FROM (
    SELECT AVG(gd.stud_grade) as aver, gd.stud_id, gd.grade_on_class, s.stud_f_name, s.stud_l_name
    FROM stud_grades AS gd
    LEFT JOIN students AS s ON gd.stud_id = s.id
    GROUP BY gd.stud_id, gd.grade_on_class, s.stud_f_name, s.stud_l_name
) AS sq
GROUP BY sq.stud_id;
