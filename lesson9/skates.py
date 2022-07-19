"""
    В прокате коньков есть разные размеры. Известно, что желающий покататься
    может надеть коньки любого размера, которые не меньше размера его ноги.

    Напишите функцию, которая принимает список доступных размеров коньков и
    список размеров ног желающих.

    И возвращает наибольшее количество людей,
    которые смогут покататься одновременно.


    Например:
    [in]
    [39, 38, 41, 37] (доступные размеры)
    [40, 39, 41] (размеры ног желающих)

    [out]
    2

    [37, 38, 39, 40] , [37, 37, 40, 40] -> 3
    [37, 38, 39, 40] , [42] -> 0
    [37, 38, 39] , [37, 37, 37, 37] -> 3

    Напишите несколько тестов
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


@time_decorator
@slow_decorator
def search(skates: list, legs: list):
    count = 0
    for leg in legs:
        if leg > max(skates):
            continue
        min_suitable_size = min(filter(lambda x: x >= leg, skates))
        skates.remove(min_suitable_size)
        count +=1
        # print(min_suitable_size)
        if len(skates) == 0:
            break
        # print(skates)
    return count


print(search(skates=[37, 38, 39], legs=[40, 37, 37, 36, 38]))


assert search([37, 38, 39, 40], [37, 37, 40, 40]) == 3
assert search([37, 38, 39, 40], [42]) == 0
assert search([37, 38, 39], [37, 37, 37, 37]) == 3