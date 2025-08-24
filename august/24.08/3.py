import sqlite3

connection = sqlite3.connect(r"Python_lessons\august\24.08\school.db")
cursor = connection.cursor()

cursor.execute('''
    INSERT INTO books (title, author, publish_date, page_value)
    VALUES ('Кубок огня', 'Джоан Роулинг', '2005-12-12', 650)
    ''')

print(cursor.lastrowid)

connection.rollback()
connection.close()