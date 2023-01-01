"""
    Необходимо написать программу, которая принимает на ввод 2 числа.
    Считает сумму чисел в отдельной функции.
    Если сумма больше 0, то вызывается функция positive,
    которая выводит сообщение 'positive',
    если меньше - функция negative, которая выводит сообщение negative.

"""


def sum_(a, b):
    return a + b


def positive():
    print('positive')


def negative():
    print('negavite')


def main():
    a = int(input('a: '))
    b = int(input('b: '))

    result = sum_(a, b)

    if result > 0:
        positive()
    else:
        negative()


if __name__ == '__main__':
    main()
