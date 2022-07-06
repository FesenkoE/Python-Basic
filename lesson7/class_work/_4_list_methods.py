"""
    Методы списков.
"""

my_list = [1, "some", "black", 8.7, 1, "python"]
print(my_list)

# 1. Добавление элемента -- append(object)

my_list.append("some")  # элемент добавляется в конец списка
print("1.", my_list)

# 2. Вставка элемента -- insert(index, object)

my_list.insert(0, "pre")  # по индексу 0 вставляем 'pre'
print("2.", my_list)

# 3. Вставка нескольких элементов ( списка ) -- extend([])

my_list.extend(["red", 34, "python"])  # элементы добавляются в конец списка
# my_list += ['red', 34, 'python']
print("3.", my_list)

# 4. Удаление элемента списка -- remove(object)
my_list.remove("red")  # удаляет первое вхождение 'red'
print("4.", my_list)

# 5. Удаление элемента списка -- pop(index),
# по умолчанию удаляет последний элемент и возвращает его

my_list.pop()  # удаляет последний элемент
tmp = my_list.pop(0)  # удаляет элемент с индексом 0 и присваевает его tmp
print("5.", my_list, tmp)

# 6. Очищение списка -- clear()

my_list_to_clear = my_list[:]  # создали копию списка

my_list_to_clear.clear()  # очищаем список

print("6.", my_list_to_clear)

# 7. Получить индекс объекта -- index(object)

print("7.", my_list.index("some", 2))

# 8. Число вхождений объекта -- count(object)

print("8.", my_list.count("some"))

second_list = [5, -2, 3, -9, 10]
print("9.", second_list)

# 10. Сортировка списка -- sort() изменяет список, в отличии от sorted()

second_list.sort()
print("10.", second_list)

# 11. Реверс -- reverse() (элементы в обратном порядке)

second_list.reverse()
print("12.", second_list)
