"""
    Определить, существует ли треугольник.

    Программа принимает на ввод 3 стороны треугольника.
    Выводит стороны и текст, существует треугольник или нет.

    * у треугольника каждая сторона меньше суммы двух других сторон
"""
is_triangle = False
side_a = 0
side_b = 0
side_c = 0

try:
    side_a = int(input('Enter side A: '))
    side_b = int(input('Enter side B: '))
    side_c = int(input('Enter side C: '))
except ValueError:
    print('Not a number')
else:
    if (side_a <= 0) or (side_b <= 0) or (side_c <= 0):
        is_triangle = False
    elif (side_a + side_b) > side_c and (side_a + side_c) > side_b and (side_b + side_c) > side_a:
        is_triangle = True
    else:
        is_triangle = False
finally:
    if is_triangle:
        print(f'Triangle with sides: {side_a}, {side_b}, {side_c} is exists')
    else:
        print(f'Triangle with sides: {side_a}, {side_b}, {side_c} is not exists')

