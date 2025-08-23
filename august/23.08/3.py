import sqlite3

connection = sqlite3.connect(r"Python_lessons\august\23.08\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]

data = [dict(zip(columns, row)) for row in rows]

for d in data:
    print(d)
    
cursor.close()