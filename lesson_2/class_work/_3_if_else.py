"""
    Инструкция if-else

    Имеет 2 варианта описания.
    1 - стандартный, 2 - строчный (обычно занимает 1 строку)

    1.      if условие:
                # здесь какой-то код
            else:
                # здесь какой-то код

    2.      True if условие else False
"""

# необходимо узнать, число отрицательное, положительное или ноль
a = int(input('a = '))

# 1 вариант
if a > 0:
    answer = 'positive'
elif a < 0:
    answer = 'negative'
else:
    answer = 'zero'

print(answer, '(standart if-else)')

# 2 вариант
answer = 'positive' if a > 0 else 'negative' if a < 0 else 'zero'

print(answer, '(string if-else)')


# Создание переменной в условии if c помощью оператора :=

a = 10
b = 20

if (result := a + b) > 25:
    print(result)
