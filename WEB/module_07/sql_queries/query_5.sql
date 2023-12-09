--query5.sql Знайти які курси читає певний викладач.

SELECT *
    FROM teachers AS t
    JOIN classes AS c on c.id  = t.teacher_class;