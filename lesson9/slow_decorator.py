"""
    Реализовать декораторы:
    1. @time_decorator - считает и выводит время работы функции,
        если функция выполняется дольше 5 секунд, тогда дополнительно
        выводить сообщение print(f'{func.__name__} - very slow function')

    * в func.__name__ лежит название функции

    2. @slow_decorator - замедляет выполнение функции на 5 секунд

    Используйте библиотеку time, а именно функции time и sleep

"""
import time


def time_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        time_of_work = time.time()-start_time
        print(time_of_work)
        if time_of_work > 5:
            print(f'{func.__name__} - very slow function')

        return result

    return wrapper


def slow_decorator(func):
    def wrapper(*args, **kwargs):
        time.sleep(5)
        result = func(*args, **kwargs)
        return result

    return wrapper