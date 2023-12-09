--query7.sql Знайти оцінки студентів у окремій групі з певного предмета.

SELECT s.stud_f_name, s.stud_l_name , sg.stud_grade, cl.class_name, s.stud_group 
    FROM students AS s
    JOIN stud_grades AS sg ON s.id = sg.stud_id
    JOIN classes as cl on cl.id = sg.grade_on_class 
    WHERE s.stud_group=1 AND cl.id=1;