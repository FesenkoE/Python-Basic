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

x = float(input('Enter point x: '))
y = float(input('Enter point y: '))

if (x > 0) and (y > 0):
    print('I quarter')
elif (x < 0) and (y > 0):
    print('II quarter')
elif (x < 0) and (y < 0):
    print('III quarter')
elif (x > 0) and (y < 0):
    print('IV quarter')
else:
    print('There are not quarter')
