import sqlite3

connection = sqlite3.connect(r"Python_lessons\august\24.08\school.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute('SELECT * FROM books')
rows = cursor.fetchall()
data = [dict(row) for row in rows]

# for d in data:
#     print(d)

for row in rows:
    print(row["title"])
    
cursor.close()