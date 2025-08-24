#  Таблица - wallets
#  Поля 
# id - первичный ключ
# teacher_id связь с таблицей teachers
# balance - число не может быть меньше 0
# is_active - булево значение


# CHECK(is_active IN (0,1))


import sqlite3

connection = sqlite3.connect(r"Python_lessons\august\24.08\school.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS wallets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id INTEGER NOT NULL,
        balance INTEGER NOT NULL CHECK(balance >= 0),
        is_active INTEGER DEFAULT 1 CHECK(is_active IN (0,1)),
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    )                                    
""")

connection.commit()