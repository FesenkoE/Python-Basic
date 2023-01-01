"""
    Множества. set - изменяемое и frozenset - неизменяемое)
    Пустое множество можно создать только с помощью set() и frozenset(),
    заполненное - с помощью литерала {} и set()/frozenset()
"""

my_list = [1, 2, 3, 2, 3, 1, 3, 1, 1]
print(my_list)  # [1, 2, 3, 2, 3, 1, 3, 1, 1]

a = set(my_list)
print(a)  # {1, 2, 3}

b = {4, 2, 2, 2, 2, 2, 2, 3, 3}
print(b)  # {2, 3, 4}


# ------------------------
# Операции и методы множеств
# ------------------------

# Операции и методы, которые не изменяю множества (доступны set и frozenset)
# Помимо описанных ниже, доступны все операции сравнения: ==, !=, <, >, <=, >=

# Объединение
print(a | b)  # {1, 2, 3, 4}
print(a.union(b))  # {1, 2, 3, 4}

# Пересечение
print(a & b)  # {2, 3}
print(a.intersection(b))  # {2, 3}

# Разница
print(a - b)  # {1}
print(a.difference(b))  # {1}
print(b - a)  # {4}
print(b.difference(a))  # {4}

# Симетричная разница (операция обратная пересечению)
print(a ^ b)  # {1, 4}
print(a.symmetric_difference(b))  # {1, 4}

# Не содержат ли множества общих элементов
print(a.isdisjoint(b))  # False

# Является ли a подмножеством b, аналог операции >=
print(a.issubset(b))  # False
print(a.issuperset(b))  # обратная операция - <=

# Сделать копию множества
c = a.copy()
print(c)  # {1, 2, 3}


# Операции и методы, которые изменяю множества (доступны только для set)

d = {"one", 2, "abc"}

d.add("new elem")  # добавляет объект в множество

# Удаление элементов
d.remove("abc")  # удаляет элемент. KeyError, если элемента нет.
d.discard("abc")  # удаляет элемент, если он существует
d.pop()  # удаляет первый элемент и возвращает его
d.clear()  # очищает множество

# Методы и операции присваивания (по 3 равносильных варианта)

# update() - объединение
# a.update(b)
# a |= b
# a = a | b

# intersection_update() - пересечение
# a.intersection_update(b)
# a &= b
# a = a & b

# difference_update() - разница
# a.difference_update(b)
# a -= b
# a = a - b

# symmetric_difference_update() - симетричная разница
# a.symmetric_difference_update(b)
# a ^= b
# a = a ^ b
