"""
    Для объявления функции используется ключевое слово def,
    после чего идет название функции, скобки и двоеточие.
    С новой строки с отступами начинается тело функции.
"""


def func():
    # тело функции
    print('Hello world!')


func()  # вызов объявленной функции


def summ(a, b):  # a и b - обязательные параметры функции
    result = a + b
    print(result)


# вызов функции сумм с передачей в нее разных аргументов
summ(5, 10)  # 5 и 10 - аргументы функции
summ(1, 19)
summ(33, 178)
summ('Hello ', 'world')


# функция может возвращать значение с помощью ключевого слова return
def summ(a, b, c):
    return a + b + c


print(summ(1, 10, 2))

# возращаемое значение функция можно присвоить переменной
a = summ(a=0, c=125, b=10)
print(a)


def usd_to_uah(currency, rate=28):  # rate - не обязательный параметр
    return currency * rate


uah = usd_to_uah(10)
print(uah)

uah = usd_to_uah(10, 28.9)
print(uah)


# функция может принимать 0 и более аргументов.
# Для этого используются операторы * (кортеж) и ** (словарь)
def func(*args, **kwargs):
    print(args)  # сюда попадают все не именованные аргументы
    print(kwargs)  # здесь - именованные


func(1, 2, 3, 4, 'python', [], 3.14, name='max', age=20)
func()
func(1)
func(a=10)


def func(number, *args, **kwargs):  # number - обязательный параметр
    print(number)
    print(args)
    print(kwargs)


func(1, 2, 3, 4, 'python', [], 3.14, name='max', age=20)
