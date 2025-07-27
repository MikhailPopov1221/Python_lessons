def test_recursion(value):
    print(f"начало функции {value}")
    if value != 0:
        test_recursion(value - 1)
    print(f"конец функции {value}")
    return value

test_recursion(3)