import sqlite3

connection = sqlite3.connect(r"Python_lessons\august\24.08\school.db")
cursor = connection.cursor()

cursor.execute('SELECT * FROM wallets')
d = cursor.description

for i in d:
    print(i[0])
    
name_list = [i[0] for i in d]
print(name_list)