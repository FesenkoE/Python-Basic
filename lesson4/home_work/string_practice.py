string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

"""
1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
   Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'
"""

string = string.replace(', ', ' ')
print(f'String: {string}')

"""
2. Найти индекс самой последней буквы 's' в строке.
   Результат: 53
"""

last_s_idx = string.rindex('s')
print(f'Last "S" index: {last_s_idx}')

"""
3. Найти количество букв 'i' в строке (регистр не имеет значения).
   Результат: 6
"""

i_counter = string.lower().count('i')
print(f'Count "i": {i_counter}')

"""
4. Найти и вывести срез строки.
   Результат: 'simply dummy text'
   (используйте методы find или index для получения индексов)
"""

idx = string.find('simply dummy text')
slicing = string[idx:idx + len('simply dummy text')]
print(f'Slicing: {slicing}')

"""
5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
   и выведите на экран.
   Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the
   printing industry.'
"""

first_part = (string[:len(string) // 2]) * 3
second_part = string[len(string) // 2:]
print(f'Result: {first_part + second_part}')
