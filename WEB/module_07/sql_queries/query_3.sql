--query3.sql Знайти середній бал у групах з певного предмета.

SELECT AVG(sg.stud_grade), s.stud_group
    FROM stud_grades AS sg
    JOIN students AS s on sg.stud_id = s.id
    WHERE sg.grade_on_class = 1
    GROUP BY s.stud_group;