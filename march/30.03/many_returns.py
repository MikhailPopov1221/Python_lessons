# def convert_to_5grade(grade):
#     if grade >= 10:
#         return 5
#     elif grade >= 7:
#         return 4
#     elif grade >= 4:
#         return 3
#     print("Convert completed")
    
# print(convert_to_5grade(12))


def convert_to_5grade(grade):
    new_grade = None
    if grade >= 10:
         new_grade = 5
    elif grade >= 7:
         new_grade = 4
    elif grade >= 4:
         new_grade = 3
    else:
        new_grade = 2      
    return new_grade


print(convert_to_5grade(12))
    