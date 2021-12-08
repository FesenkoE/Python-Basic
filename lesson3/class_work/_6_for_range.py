"""
    Для генерации числовых последовательностей используется функция range()

    range(start[, end[, step])

    В математике - последовательность [start; end) - т.е. end не включается
"""

range(10)  # 0 1 2 3 4 5 6 7 8 9
range(1, 7)  # 1 2 3 4 5 6
range(1, 10, 2)  # 1 3 5 7 9

# обратный порядок последовательности
range(10, 1, -2)  # 10 8 6 4 2


for i in range(10):
    print(i)


for i in range(1, 11):
    print(i)


for i in range(2, 21, 2):
    print(i)
