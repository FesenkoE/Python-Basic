"""
    Определить, существует ли треугольник.

    Программа принимает на ввод 3 стороны треугольника.
    Выводит стороны и текст, существует треугольник или нет.

    * у треугольника каждая сторона меньше суммы двух других сторон
"""

side_a = int(input('Enter side A: '))
side_b = int(input('Enter side B: '))
side_c = int(input('Enter side C: '))

if side_a + side_b > side_c and side_b + side_c > side_a and side_c + side_a > side_b:
    print('Triangle is exists')
else:
    print('Triangle is not exists')


