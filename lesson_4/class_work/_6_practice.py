"""
    1. Вводим строку.
        Вывести первые три символа в верхнем регистре и
    последние три символа в нижнем регистре, если длина строки больше 5.
        Иначе вывести первый символ с измененным регистром столько раз,
    какова длина строки.
"""

# s = input('1. Enter some string: ')

s = "Hello woRlD"

if len(s) > 5:
    print(s[:3].upper(), s[-3:].lower())
else:
    print(s[0].swapcase() * len(s))

"""
    2. Определить, является ли строка палиндромом.
    aba == aba
    anna == anna
    python != nohtyp
"""

"""
    3. Удалить из строки повторяющиеся символы и пробелы.

    for
    find()
"""

# s = input('3. Enter some string: ')
s = "Hello woR lD"

"""
    4. Посчитать количество цифр, строчных и заглавных букв в строке.
"""

# s = input('4. Enter some string: ')
s = "pyth$on DjangO 123 %@#2020 Basic!"
specials = ''
counter_d = counter_l = counter_u = 0

for char in s:
    if char.isdigit():
        counter_d += 1
    elif char.islower():
        counter_l += 1
    elif char.isupper():
        counter_u += 1
    elif not char.isspace():
        specials += char

print(counter_d, counter_l, counter_u)
print(specials)
