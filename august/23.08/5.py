import sqlite3

connection = sqlite3.connect(r"Python_lessons\august\23.08\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute("SELECT * FROM workers")
rows = cursor.fetchall()

columns = [desc[0] for desc in cursor.description]
print(columns)


cursor.close()