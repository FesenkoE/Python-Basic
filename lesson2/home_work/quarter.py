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
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))
except ValueError:
    print('Not a number')
else:
    if (x > 0) and (y > 0):
        print('Dot is in I quarter')
    elif (x < 0) and (y > 0):
        print('Dot is in II quarter')
    elif (x < 0) and (y < 0):
        print('Dor is in III quarter')
    elif (x > 0) and (y < 0):
        print('Dot is in IV quarter')
    elif (x == 0) and (y > 0):
        print('Dot is in I and II quarter')
    elif (x == 0) and (y < 0):
        print('Dot is in III and IV quarter')
    elif (x > 0) and (y == 0):
        print('Dot is in I and IV quarter')
    elif (x < 0) and (y == 0):
        print('Dot is in II and III quarter')
    else:
        print('Dot is in center')


