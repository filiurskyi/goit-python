--query4.sql Знайти середній бал на потоці (по всій таблиці оцінок).

SELECT AVG(sg.stud_grade)
    FROM stud_grades AS sg
    JOIN students AS s on sg.stud_id = s.id;