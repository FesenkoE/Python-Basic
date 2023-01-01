"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
    если больше в верхнем - вывести все в верхнем,
    если поровну - вывести в противоположных регистрах.

    2. Если в строке каждое слово начинается с заглавной буквы, тогда
    добавить в начало строки 'done. '.
    Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)

    3. Если длина строки больше 20, то обрезать лишние символы до 20.
    Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))

    После выполнения кажого пункта выводить результат типа:
    1. Исходная строка: "some string".
    Результат: "some edited string".
    (Использовать форматирование строк f либо метод format)
"""
#1
# можно заменить данную строку на input()
string = 'Lorem, LLL'
count_upper = 0
count_lower = 0
for char in string:
    if char.isupper():
        count_upper += 1
    elif char.islower():
        count_lower += 1
if count_lower > count_upper:
    new_string = string.lower()
elif count_lower < count_upper:
    new_string = string.upper()
else:
    new_string = string.swapcase()
    # for ch in string:
    #     ch = ord(ch)
    #     if 65 <= ch <= 90:
    #         ch = ch + 32
    #     else:
    #         ch = ch - 32
    #     new_str += chr(ch)
    # print(new_str)
print(f'верхний: {count_upper}, нижний: {count_lower}')
print(f'Исходная строка: "{string}"\nРезультат: "{new_string}')
print('__________________________')


#2

string2 = 'Lorem, lLLLL'
last_char = ''
flag_title = None
for char in string2:  # соченил проверку, а потом уже узнал что есть метод .istitle
    if char.isalpha() and not last_char.isalpha():  # сейчас символ алфавита, а прдидущий нет
        if char.isupper():  # и он заглавный
            flag_title = 1  # при каждом начале слова с заглавной буквы флаг выставляем == 1
        else:
            flag_title = 0  # если попадается хоть одна не заглавная буква на ней флаг = 0 и цикл останавливается
            break
    last_char = char  # текущий символ становится предидущим символом

if flag_title:
    new_string2 = 'done. ' + string2
else:
    new_string2 = 'draft: ' + string2[5:]

print(f'Исходная строка: "{string2}"\nРезультат: "{new_string2}')
print('__________________________')


#3

string3 = 'Lorem, lLLLL1234567891011121314'
if len(string3) < 20:
    new_string3 = string3.ljust(20, '@')
elif len(string3) > 20:
    new_string3 = string3[:21]
print(f'Исходная строка: "{string3}"\nРезультат: "{new_string3}')
print('__________________________')