import sqlite3


with sqlite3.connect(r"Python_lessons\august\24.08\school.db") as connection:
    cursor = connection.cursor()
    cursor.execute('''
    SELECT author, COUNT(id) AS v
    FROM books
    GROUP BY author
    ORDER BY v DESC
    ''')
    
    rows = cursor.fetchall()
    for row in rows:
        print(*row)
        # print(row[0], row[1])
        
        
print("sdgehrjr")
        