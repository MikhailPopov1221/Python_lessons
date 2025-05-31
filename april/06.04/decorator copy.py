def new_abillity(func):
    def wrapper():
        print("Функционал перед функцией")
        func()
        print("Функционал после функции")
    return wrapper


# hello = new_abillity(hello)

@new_abillity
def hello():
    print('Hello world!')
    
hello()

