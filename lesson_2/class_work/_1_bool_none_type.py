"""
    Логический тип данных bool
    Может иметь значение True либо False
"""

active = True
deleted = False

print(active, type(active))  # True <class 'bool'>
print(deleted, type(deleted))  # False <class 'bool'>

"""
    bool находится в подмножестве int, поэтому преобразовывается в числа
    и для него доступны все арифметические операции, как и для чисел
"""

print(int(active))  # 1
print(int(deleted))  # 0
print(True + True)  # 2
print(2 + True * False ** 0)  # 3


"""
    Приведение к типу bool
"""

# 1. Числа
# все числа, кроме 0 - True, сам 0 - False
a = 0
b = -123
print(bool(a))  # False
print(bool(b))  # True

# 2. Последовательности (строки, списки, кортежи, множества, словари)
# пустая последовательность - False, заполненная - True
print(bool(''))  # False
print(bool(' '))  # True
print(bool([0, 0, 0]))  # True

"""
    Тип данных NoneType
    Для хранения пустых значений используется None
"""

status = None

print(status, type(status))  # None <class 'NoneType'>
