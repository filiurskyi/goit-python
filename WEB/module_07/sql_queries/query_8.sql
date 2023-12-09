--query8.sql Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT AVG(sg.stud_grade), t.teacher_f_name, t.teacher_l_name, c.class_name 
    FROM stud_grades AS sg
    JOIN classes AS c ON c.id = t.teacher_class
    JOIN teachers AS t ON sg.grade_on_class = t.teacher_class
    GROUP BY sg.grade_on_class;