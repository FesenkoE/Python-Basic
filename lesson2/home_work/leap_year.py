"""
    Вводится год.
    Программа выводит количество дней в году, учитывая високосный год.

    * високосный год кратный 4, но не кратный 100 или кратный 400
"""

days = 365

try:
    year = int(input('Enter year: '))
except ValueError:
    print('Not valid value')
else:
    if (year % 4) == 0 and year % 100 != 0 or year % 400 == 0:
        days = 366

    print(f'In {year} {days} days')




