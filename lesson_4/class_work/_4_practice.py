"""
    1. Если в строке буква 's' встречается один раз, вывести ее индекс,
    если 2 и более - вывести индекс ее первого и последнего вхождения.

    Для теста:
    'expressions'
    'string'
    'python'
"""

string = "expressions"

if string.count('s') == 1:
    print(string.index('s'))
elif string.count('s') >= 2:
    print(string.index('s'), string.rindex('s'))

"""
    2. Переставить слова местами.
    Возвести первую букву получившейся строки в верхний регистр,
    все остальный в нижний.
"""
s = 'Hello world'
idx = s.index(' ')
s = s[idx + 1:] + ' ' + s[:idx]
print(s.capitalize())

"""
    3. В строке заменить цифры словами
    0 - zero
    1 - one
    2 - two
    3 - three
    4 - four

    Для теста:
    '2 + 2 = 4'
    '1,2,3,4,5'
    'He11o W0rld'
"""

s = '2 + 2 = 4'

print(s.replace('2', 'two').replace('4', 'four'))

"""
    4. Удалить из строки все запятые.
"""

s = "Secure, shy, favour length, all twenty, denote."

print(s.replace(',', ''))
