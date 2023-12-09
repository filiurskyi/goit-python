--query9.sql Знайти список курсів, які відвідує студент.

SELECT c.class_name 
	FROM students AS s
	JOIN stud_grades AS sg ON sg.stud_id = s.id 
	JOIN classes AS c ON sg.grade_on_class = c.id
	WHERE s.id = 2
	GROUP BY c.class_name 
	;