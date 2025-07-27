class Queue:
    def __init__(self, max_items):
        self.items = []
        self.max_items = max_items
        
    def push(self, item):
        if self.size() < self.max_items:
            self.items.append(item)
        else:
            raise Exception("Очередь переполнена")
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Очердь пуста")
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Очердь пуста")
        else:
            return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    


def show_menu():
    print("Выберите операцию:")
    print("1 - Создать очередь")
    print("2 - Добавить элемент в очередь")
    print("3 - Забрать элемент из очереди")
    print("4 - Выход")

while True:    
    show_menu()
    choise = int(input())
    
    if choise == 1:
        q = Queue(5)
        print("Очередь создана!")
    elif choise == 2:
        try:
            print("Введите элемент для добавления")
            elem = int(input())
            q.push(elem)
            print(f"Элемент {elem} добавлен в очередь")
        except:
            print("Ошибка добавления элемента")
    elif choise == 3:
        try:
            elem = q.pop()
            print(f"Получен элемент: {elem}")
        except:
            print("Ошибка получения элемента")
    
    elif choise == 4:
        break  
    else:
        print("Введена некорректная команда")
        
    input("Нажмите для продолжения")
        
            
            