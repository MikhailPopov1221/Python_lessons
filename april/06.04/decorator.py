def hello():
    print('Hello world!')
    
# hello()

def new_abillity(func):
    def wrapper():
        print("Функционал перед функцией")
        func()
        print("Функционал после функции")
    return wrapper
    
# new_abillity(hello)
hello = new_abillity(hello)

hello()

