import sqlite3

connection = sqlite3.connect(r"Python_lessons\august\23.08\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute("DELETE FROM workers WHERE id = ?", (2,))

connection.commit()

cursor.execute("SELECT * FROM workers")
rows = cursor.fetchall()

# print(rows)

for row in rows:
    print(row)
    
cursor.close()