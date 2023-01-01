"""
    Вводится год.
    Программа выводит количество дней в году, учитывая високосный год.

    * високосный год кратный 4, но не кратный 100 или кратный 400
"""

year = int(input('Enter year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('There are 366 days in the year')
else:
    print('There are 365 days in the year')




