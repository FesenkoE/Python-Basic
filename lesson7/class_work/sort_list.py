"""
    Напишите функцию, которая принимает список чисел
    и возвращает отсортированный список,
    при условии, что все числа -1 остаются на своих местах.

    [in]   [6, 3, -1, 4, 2, -1, 1]
    [out]  [1, 2, -1, 3, 4, -1, 6]
"""


# 1 вариант
def sort_ascending(x):
    tmp = sorted([i for i in x if i != -1])
    sorted_list = []
    idx = 0
    for i in x:
        if i != -1:
            sorted_list.append(tmp[idx])
            idx += 1
        else:
            sorted_list.append(i)
    return sorted_list


# 2 вариант
def sort_ascending(x):
    for i in range(len(x)):
        if x[i] == -1:
            continue
        else:
            min_number_index = i
        for k in range(i + 1, len(x)):
            if x[k] == -1:
                continue
            elif x[k] < x[min_number_index]:
                min_number_index = k
        x[i], x[min_number_index] = x[min_number_index], x[i]
    return x


# 3 вариант
def sort_ascending(x: list) -> list:
    new_list = sorted([i for i in x if i != -1])

    for idx in range(len(x)):
        if x[idx] != -1:
            x[idx] = new_list.pop(0)

    # for index, value in enumerate(x):
    #     if value != -1:
    #         x[index] = new_list.pop(0)

    # строчки 42-44 делают тоже самое, что и строчки 46-48

    return x


# 4 вариант
def sort_ascending(x: list) -> list:
    temp_2 = [j for j in range(len(x)) if x[j] == -1]
    x.sort()
    x = [j for j in x if j > 0]
    for q in temp_2:
        x.insert(q, -1)
    return x


# 5 вариант (генератор и enumerate)
def sort_ascending(x):
    tmp = [i for i in x if i != -1]
    g = (i for i in sorted(tmp))
    for index, value in enumerate(x):
        if value > 0:
            x[index] = next(g)
    return x


t_1 = [-1, 150, 190, 170, -1, -1, 160, 180]
assert sort_ascending(t_1) == [-1, 150, 160, 170, -1, -1, 180, 190]

t_2 = [-1, -1, -1, -1, -1]
assert sort_ascending(t_2) == [-1, -1, -1, -1, -1]

t_3 = [4, 2, 9, 11, 2, 16]
assert sort_ascending(t_3) == [2, 2, 4, 9, 11, 16]

t_4 = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
assert sort_ascending(t_4) == [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]

t_5 = [-1]
assert sort_ascending(t_5) == [-1]

print("All tests passed successfully!")
