"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.

    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)

    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))

    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "some string".
        Результат: "some edited string".
    (Использовать форматирование строк f либо метод format)
"""

string = 'Lorem, IPsUM, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY.'
count_lower = 0
count_upper = 0
result = ''

for char in string:
    if char.islower():
        count_lower += 1
    elif char.isupper():
        count_upper += 1

if count_lower > count_upper:
    result = string.lower()
elif count_lower < count_upper:
    result = string.upper()
else:
    result = string.swapcase()

print(
    f'Исходная строка: {string}\n'
    f'Результат: {result}'
)

if string.istitle():
    result = 'done. ' + string
else:
    result = 'draft. ' + string[5:]

print(
    f'Исходная строка: {string}\n'
    f'Результат: {result}'
)

if len(string) > 20:
    result = string[:20]
else:
    result = string.ljust(20, '@')

print(
    f'Исходная строка: {string}\n'
    f'Результат: {result}'
)