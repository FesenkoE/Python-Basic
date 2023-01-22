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


def main():
    def time_decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func()
            print(f'time left: {time.time() - start}')

        return wrapper

    def slow_decorate(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            time.sleep(5)
            print(f'time left: {time.time() - start}')

        return wrapper

    @time_decorator
    def some_func():
        print('This success expression')

    @slow_decorate
    def slow_func():
        print('This slow function')

    some_func()
    slow_func()


if __name__ == '__main__':
    main()
