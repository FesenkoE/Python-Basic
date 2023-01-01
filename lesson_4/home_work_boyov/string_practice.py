string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

"""
    1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'
"""

"""
    2. Найти индекс самой последней буквы 's' в строке.
    Результат: 53
"""

"""
    3. Найти количество букв 'i' в строке (регистр не имеет значения).
    Результат: 6
"""

"""
    4. Найти и вывести срез строки.
    Результат: 'simply dummy text'
    (используйте методы find или index для получения индексов)
"""

"""
    5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
    и выведите на экран.
    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the 
    printing industry.'
"""
#1
string = string.replace(',', '')
print(string)
#2
print(string.rfind('s'))
#3
print(string.lower().count('i'))
#4
print(string[string.find('simply'):string.rfind('text')+4])
#5
string = string[:len(string)//2] * 3 + string[len(string)//2:]
print(string)