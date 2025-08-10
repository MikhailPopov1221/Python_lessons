import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "school.db"

# Подключение
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Сброс таблиц
cursor.executescript("""
DROP TABLE IF EXISTS student_course;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS teachers;
""")

# Таблицы
cursor.execute("""
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    teacher_id INTEGER NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);
""")

cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER CHECK (age >= 0)
);
""")

cursor.execute("""
CREATE TABLE student_course (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
""")

# Данные
teachers = [
    ("Иван Петров", "Математика"),
    ("Мария Смирнова", "Информатика"),
    ("Ольга Иванова", "История")
]
cursor.executemany("INSERT INTO teachers (name, department) VALUES (?, ?)", teachers)

courses = [
    ("Алгебра", 1),
    ("Геометрия", 1),
    ("Программирование на Python", 2),
    ("Веб-разработка", 2),
    ("История Древнего мира", 3)
]
cursor.executemany("INSERT INTO courses (title, teacher_id) VALUES (?, ?)", courses)

students = [
    ("Алексей Сидоров", 16),
    ("Елена Кузнецова", 17),
    ("Дмитрий Орлов", 16),
    ("Светлана Лебедева", 15)
]
cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", students)

student_course = [
    (1, 1), (1, 3),
    (2, 2), (2, 3), (2, 4),
    (3, 5),
    (4, 1), (4, 2),
]
cursor.executemany("INSERT INTO student_course (student_id, course_id) VALUES (?, ?)", student_course)

# Сохраняем и закрываем
conn.commit()
cursor.close()
conn.close()

print(f"База данных '{DB_PATH.name}' создана и заполнена.")