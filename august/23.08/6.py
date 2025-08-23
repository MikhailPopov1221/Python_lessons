import sqlite3

connection = sqlite3.connect(r"Python_lessons\august\23.08\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

new_woker = ('Павел', 55, 'сварщик')

cursor.execute("""
INSERT INTO workers (name, age, profession)
VALUES (?, ?, ?)                           
""", new_woker)

connection.commit()

cursor.execute("SELECT * FROM workers")
rows = cursor.fetchall()

# print(rows)

for row in rows:
    print(row)
    
cursor.close()