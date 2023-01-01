"""
    1. Записать в файл practice.txt: числа от 9 до 17 через пробел
    2. Прочитать этот файл и вывести содержимое и тип содержимого на экран
    3. В файл с новой строки записать такой текст: Some text 123, @!$!@SA
    4. Прочитать файл и вывести в консоль:
        - количество заглавных букв.
        - количество строчных букв.
        - количество цифр.
        - количество спецсимволов.
"""

# 1. Записать в файл practice.txt: числа от 9 до 17 через пробел

# 1 вариант
with open("practice.txt", "w") as f:
    for i in range(9, 18):
        f.write(f"{i} ")

# 2 вариант
with open("practice.txt", "w") as f:
    for i in range(9, 18):
        print(i, end=" ", file=f)

# 3 вариант (best)
with open("practice.txt", "w") as f:
    digits = " ".join(str(i) for i in range(9, 18))
    f.write(digits)


# 2. Прочитать этот файл и вывести содержимое и тип содержимого на экран

with open("practice.txt") as f:
    data = f.read()
    print(data, type(data))


# 3. В файл с новой строки записать такой текст: Some text 123, @!$!@SA

with open("practice.txt", "a") as f:
    f.write("\nSome text 123, @!$!@SA")
    # or
    # print('\nSome text 123, @!$!@SA', file=f)


# 4.

with open("practice.txt") as f:
    data = f.read()

    counter_l = counter_u = counter_d = counter_s = 0
    for i in data:
        if i.islower():
            counter_l += 1
        elif i.isupper():
            counter_u += 1
        elif i.isdigit():
            counter_d += 1
        elif not i.isspace():
            counter_s += 1

    print(
        f"Lowers: {counter_l}\n"
        f"Uppers: {counter_u}\n"
        f"Digits: {counter_d}\n"
        f"Specials: {counter_s}"
    )


# Все 4 пункта вместе
with open("practice.txt", "w+") as f:
    # 1.
    digits = " ".join(str(i) for i in range(9, 18))
    f.write(digits)

    # 2.
    f.seek(0)
    data = f.read()
    print(data, type(data))

    # 3.
    f.write("\nSome text 123, @!$!@SA")

    # 4.
    f.seek(0)
    data = f.read()

    counter_l = counter_u = counter_d = counter_s = 0
    for i in data:
        if i.islower():
            counter_l += 1
        elif i.isupper():
            counter_u += 1
        elif i.isdigit():
            counter_d += 1
        elif not i.isspace():
            counter_s += 1

    print(
        f"Lowers: {counter_l}\n"
        f"Uppers: {counter_u}\n"
        f"Digits: {counter_d}\n"
        f"Specials: {counter_s}"
    )
