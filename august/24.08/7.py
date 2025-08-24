import sqlite3

connection = sqlite3.connect(r"Python_lessons\august\24.08\school.db")
cursor = connection.cursor()


new_wallets = [
    (1, 100),
    (2, 100),
    (3, 100)
]

cursor.executemany(""" 
    INSERT INTO wallets (teacher_id, balance)
    VALUES (?,?)              
    """,
    new_wallets)

connection.commit()