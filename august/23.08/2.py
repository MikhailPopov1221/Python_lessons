import sqlite3

connection = sqlite3.connect(r"Python_lessons\august\23.08\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute("SELECT books.title FROM books")
rows = cursor.fetchall()

# print(rows)

for row in rows:
    print(row)
    
cursor.close()