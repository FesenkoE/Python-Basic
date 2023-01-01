"""
    Вывести периметр и площадь прямоугольника.
    Стороны прямоугольника вводятся с помощью input().

    Периметр - сумма всех сторон прямоугольника (удвоенная сумма 2х сторон)
    Площадь - произведение 2х сторон прямоугольника.
"""

side_a = int(input('Enter side A: '))
side_b = int(input('Enter side B: '))

perimeter = side_a * 2 + side_b * 2
area = side_a * side_b

print('Perimeter: ', perimeter)
print('Area: ', area)
