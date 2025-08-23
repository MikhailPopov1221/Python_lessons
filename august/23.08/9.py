import sqlite3

connection = sqlite3.connect(r"Python_lessons\august\23.08\school.db")
cursor = connection.cursor()

def add_new_worker(name, age, profession):
    cursor.execute("""
    INSERT INTO workers (name, age, profession)
    VALUES (?, ?, ?)                           
    """, (name, age, profession))

    connection.commit()

def delete_worker(worker_id):
    cursor.execute("DELETE FROM workers WHERE id = ?", (worker_id,))
    connection.commit()

def show_workers():
    cursor.execute("SELECT * FROM workers")
    rows = cursor.fetchall()

    for row in rows:
        print(row)


def print_menu():
    print("1 - Добавить нового работника")
    print("2 - Удалить работника по его id")
    print("3 - Показать всех работников")
    print("4 - Выход")

while True:
    print_menu()
    choice = input("Введите номер команды: ")
    try:
        choice = int(choice)
    except:
        print("Введены некорректные данные")
        input("Нажмите любую кнопку для продолжения")
        continue
    
    if choice == 1:
        name = input("Введите имя работника: ")
        age = int(input("Введите возраст работника: "))
        prof = input("Введите профессию работника: ")
        
        add_new_worker(name, age, prof)
        print("Операция успешно выполнена!")
        
    elif choice == 2:
        id = int(input("Введите номер id: "))
        delete_worker(id)
        print("Операция успешно выполнена!")
    elif choice == 3:
        show_workers()
        
    elif choice == 4:
        break
    else:
        print("Данная команда отсутствует")
    input("Нажмите любую кнопку для продолжения")

