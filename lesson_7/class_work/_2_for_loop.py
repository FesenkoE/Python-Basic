colors = ["red", "yellow", "orange", "green", "blue", "violet"]

# Цикл проходит по каждому элементу списка colors и выполняет тело цикла
for color in colors:
    # тело цикла

    if "a" in color:
        continue
    elif "b" in color:
        break

    print(color)
else:
    # если цикл был закончен не с помощью break, то выполняется этот блок
    print('"b" not found in any elements')

# Обход циклом вложенных списков
my_list = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]

for i in my_list:
    for j in i:
        print(j)

# Создание нового списка квадратов чисел из старого
old_list = [1, 2, 3, 4, 5]

# 1 способ
new_list = []
for i in old_list:
    new_list.append(i ** 2)

print(new_list)

# 2 способ (конструктор списков - аналог первого способа)
new_list = [i ** 2 for i in old_list]

print(new_list)


# только для нечетных чисел из списка old_list

# 1 способ
new_list = []
for i in old_list:
    if i % 2 != 0:
        new_list.append(i ** 2)

print(new_list)

# 2 способ (конструктор списков - аналог первого способа)
new_list = [i ** 2 for i in old_list if i % 2 != 0]
