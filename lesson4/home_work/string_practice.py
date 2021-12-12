string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'

string = string.replace(',', '')
print(f'first task {string}')

# 2. Найти индекс самой последней буквы 's' в строке.
#    Результат: 53
idx = string.rindex('s')
print(f'the last "s" index: {idx}')

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6
counter_i = string.lower().count('i')
print(f'Count "i" in string: {counter_i}')

# 4. Найти и вывести срез строки.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)
idx = string.find('simply dummy text')
print(string[idx:idx + len('simply dummy text')])

# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the
#    printing industry.'

idx = len(string) // 2
result = string[:idx]
print(string[:idx] * 3 + string[idx:])
