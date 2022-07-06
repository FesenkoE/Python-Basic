# Дан список целых чисел my_list.
my_list = [1, -2, 16, -13, 20, 0, 3, 77, 225, -42, -10, 21, 523]

# 1.
# Поменять местами 1 и последний элемент списка.

my_list[0], my_list[-1] = my_list[-1], my_list[0]


# 2.
# Создать новый список состоящий из элементов my_list, при этом заменив
# отрицательные числа на -1,
# положительные - на число 1, ноль оставить без изменений.
# Вывести 2 списка.

# 1 способ
result = []
for i in my_list:
    if i > 0:
        i = 1
    elif i < 0:
        i = -1
    result.append(i)

print(my_list)
print(result)


# 2 способ с использованием функции
def func(i):
    if i > 0:
        i = 1
    elif i < 0:
        i = -1
    return i


result = [func(i) for i in my_list]


# 3.
# Разделить исходный список на два списка
# с положительными и отрицательными числами.
# Вывести максимальное и минимальное значение каждого списка.
positive_list = []
negative_list = []
for i in my_list:
    if i > 0:
        positive_list.append(i)
    elif i < 0:
        negative_list.append(i)

print(min(positive_list), max(positive_list))
print(min(negative_list), max(negative_list))


# 4.
# Создайте список,
# в котором содержатся только нечетные числа из списка my_list

odd_list = []
for i in my_list:
    if i % 2 != 0:
        odd_list.append(i)

# Либо с помощью конструктора списков
odd_list = [i for i in my_list if i % 2 != 0]
print(odd_list)


# 5.
# Создайте список,
# в котором содержатся квадраты отрицательных чисел из списка my_list
negative_squares = [i ** 2 for i in my_list if i < 0]
print(negative_squares)
