"""
    Форматирование строк.

    Например, на ввод получаем name и age.
    Необходимо вывести результат типа:
    My name is Max. I am 21
"""

name = input('Enter name: ').capitalize()
age = input('Enter age: ')

# Как реализовать без форматирования
print('My name is ', name, '! I am ', age, sep='')
print('My name is ' + name + '! I am ' + age)


# Форматирование с помощью метода .format()
template_1 = 'My name is {}! I am {}.'
template_2 = 'My name is {0}! I am {0}.'
template_3 = 'My name is {f_name}! I am {f_age}.'

print(template_1.format(name, age))
print(template_2.format(name))  # My name is Max! I am Max.
print(template_3.format(f_age=age, f_name=name))


# Форматирование с помощью префикса f''
# В строку сразу вставляются те значения, которые записаны в фигурных скобках.
print(f'My name is {name}! I am {age}.')
print(f'My name is {input("name: ").title()}! I am {input("age: ")}.')


# Форматирование с помощью %
print('My name is %s! I am %s.' % (name, age))
print('My name is %(f_name)s! I am %(f_age)s.' % {'f_name': name, 'f_age': age})
