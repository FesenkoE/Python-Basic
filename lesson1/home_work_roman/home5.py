"""
    Вывести площадь и периметр прямоугольного треугольника.
    Катеты вводятся с помощью input().

    Площадь - произведение катетов деленное на 2.
    Периметр - сумма 3х сторон треугольника.

    * используйте теорему Пифагора: c ** 2 == a ** 2 + b ** 2
    * чтоб взять квадратный корень достаточно возвести в степень 0.5
"""

c = (a**2 + b**2)**0.5
area = (a*b) / 2
perimeter = a + b + c
print('Площадь',area)
print('Периметр', Периметр)