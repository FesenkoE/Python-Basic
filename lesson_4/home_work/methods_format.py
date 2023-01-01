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

# можно заменить данную строку на input()
string = 'Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY.'

upper_count = 0
lower_count = 0

print(f'String: {string}')

for char in string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

if upper_count > lower_count:
    edited_string = string.upper()
elif upper_count < lower_count:
    edited_string = string.lower()
else:
    edited_string = string.swapcase

print(f'Edited String: {edited_string}')

if string.istitle():
    edited_string = 'done. ' + string
else:
    edited_string = 'draft: ' + string[5:]

print(f'Edited string: {edited_string}')

if len(string) > 20:
    edited_string = string[:20]
else:
    edited_string = string.ljust(20, '@')

print(f'Edited string: {edited_string}')
