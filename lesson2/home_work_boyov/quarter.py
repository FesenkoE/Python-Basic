"""
    Программа принимает на ввод координаты точки - x и y.
    Выводит, в какой четверти системы координат лежит точка.

                ^ y
                |
            II  |    I
                |
        --------=-------->
                |         x
            III |    IV
                |
"""

try:
    x = float(input('x: '))
    y = float(input('y: '))
    if (x > 0) and (y > 0):
        print('in I')
    elif (x < 0) and (y > 0):
        print('in II')
    elif (x < 0) and (y < 0):
        print('in III')
    elif (x > 0) and (y < 0):
        print('in IV')
    elif y == 0:
        print("Point on the axis 'X'")
    elif x == 0:
        print("Point on the axis 'Y'")

except:
    print('Incorrect coordinates')
