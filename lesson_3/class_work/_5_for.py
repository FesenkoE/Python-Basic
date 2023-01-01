"""
    Цикл for используется для обхода всех элементов последовательности.

    for number in 1, 2, 3, 4, 5:
        print(number)

    Тело цикла выполняется столько раз, сколько элементов в последовательности.
"""

for i in 1, 2, 3, 4, 5:
    print(i)
else:
    # блок else выполняется в том случае, если не был вызван break
    print("расчет окончен")


for char in "Hello world!":

    if char == " ":
        # если встречается пробел, то итерация прерывается
        continue

    if char == "w":
        # если встречается 'w', то цикл прерывается
        break

    print(char)


for char in "Hello world!":
    if char == " ":
        break
else:
    print("в строке пробелов нет.")
