--query10.sql Список курсів, які певному студенту читає певний викладач.

SELECT *
	FROM students AS s
	JOIN stud_grades AS sg ON sg.stud_id = s.id
	JOIN teachers AS t ON t.teacher_class = c.id 
	JOIN classes AS c ON sg.grade_on_class = c.id
	WHERE s.id = 2 AND t.id = 1
	GROUP BY c.class_name 
	;