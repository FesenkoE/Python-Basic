my_list = [1, 2, 3, 4, 5]

# копирование списка (создание независимого дубликата)

b = list(my_list)  # первый способ копирования
c = my_list[:]  # второй способ

# создание ссылки (при изменении d - будет изменятся и my_list)
d = my_list

print('список my_list:', my_list, id(my_list))
print('список b:', b, id(b))
print('список c:', c, id(c))
print('список d:', d, id(d))


first_list = ['a', 's', 'h', 'word']
second_list = ['e', 'w', 'g']

# Сложение (конкатенация) списков
print(first_list + second_list)

# Умножение (дублирование) списков
print(first_list * 2)

# Распаковка списков
first, second, third = ['red', 'green', 'blue']

print(first, second, third)


# ВСТРОЕННЫЕ ФУНКЦИИ PYTHON

numbers = [8, 6, -12, 21, 32, -5, 7, 16]

# Минимальное и максимальное значение списка с помощью min() и max()
print('min =', min(numbers))
print('max =', max(numbers))

words = ['g', 's', 'S', 's', '1', 'u', 'W', 'a', '0']

# Сортировка с помощью sorted не изменяет список, а возвращает отсортированный
# sorted(list[, key[, reverse]])

# print(sorted(words))
print(sorted(words, reverse=True))
print(words)

# reversed() не изменяет список, а возвращает генератор* списка
print(list(reversed(numbers)))
print(numbers)

# Удаление всего списка либо конкретных его элементов по индексу
del words[0:2]

print(words)

# Длина списка (количество элементов) с помощью len()

print(len(words))

# оператор вхождения -- in
print('a' in ['ah', 'd', 'j', 'y', 'o'])
print('a' in ['a', 'd', 'j', 'y', 'o'])
