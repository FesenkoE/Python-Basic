"""
    Определить, существует ли треугольник.

    Программа принимает на ввод 3 стороны треугольника.
    Выводит стороны и текст, существует треугольник или нет.

    * у треугольника каждая сторона меньше суммы двух других сторон
"""

try:
    a = float(input("Enter side 'a' of the triangle: "))
    b = float(input("Enter side 'b' of the triangle: "))
    c = float(input("Enter side 'c ' of the triangle: "))

    if (a + b > c) and (b + c > a) and (c + a > b):
        print('Triangle: {}, {}, {}.'.format(a, b, c))
    else:
        print('Not triangle: {}, {}, {}.'.format(a, b, c))

except ValueError:
    print('Not valid value')
