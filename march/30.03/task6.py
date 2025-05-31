def is_simple_number(number):
    for delitel in range(2, number):
        if number % delitel == 0:
            return False
    return True


print(is_simple_number(7))
print(is_simple_number(6))