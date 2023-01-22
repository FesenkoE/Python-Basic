data = [
    (2, "green"),
    (1, "blue"),
    (2, "yellow"),
    (1, "aquamarine"),
    (4, "red"),
    (3, "gold"),
    (5, "black"),
    (2, "brown"),
    (5, "pink"),
    (1, "purple"),
    (4, "white"),
    (1, "gray"),
]


# 1. Вывести список data, отсортированный по цвету (2 элемент кортежа).
color_sorted = sorted(data, key=lambda d: d[1])
print(f'Sorted by color: {color_sorted}')

# 2. Отсортировать список по 1 элементу кортежа, а если значения одинаковые,
#    то их отсортировать по 2 элементу. Результат вывести на экран.
color_sorted = sorted(data, key=lambda d: (d[0], d[1]))
print(f'Sorted by number: {color_sorted}')

# 3. С помощью filter() и lambda вывести только те кортежи из списка,
#    цвет которых состоит из 4 букв.
color_filtered = list(filter(lambda d: len(d[1]) == 4, data))
print(f'Filtered Color: {color_filtered}')

# 4. Вывести цвет, которой состоит из наибольшего количества букв.
max_len_word = max(data, key=lambda d: len(d[1]))
print(f'Max Len Color: {max_len_word[1]}')
