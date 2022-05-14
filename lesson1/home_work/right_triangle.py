"""
    Вывести площадь и периметр прямоугольного треугольника.
    Катеты вводятся с помощью input().

    Площадь - произведение катетов деленное на 2.
    Периметр - сумма 3х сторон треугольника.

    * используйте теорему Пифагора: c ** 2 == a ** 2 + b ** 2
    * чтоб взять квадратный корень достаточно возвести в степень 0.5
"""

side_a = int(input('Enter side A: '))
side_b = int(input('Enter side B: '))

side_c = (side_a ** 2 + side_b ** 2) ** 0.5
area = (side_a + side_b) / 2
perimeter = side_a + side_b + side_c

print('Area: ', area)
print('Perimeter: ', perimeter)
