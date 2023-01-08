"""
    В библиотеке time есть 2 полезные функции

    time.time() - возвращает текущую дату и время в Unix-формате (секундах)
    time.sleep(seconds) - приостанавливает выполнение кода на seconds секунд

    * Unix-время - количество секунд, прошедших с 1 января 1970 года
"""
import time


def func_1():
    list_ = []
    for i in range(10 ** 6):
        list_.append(i)
    return list_


def func_2():
    return [i for i in range(10 ** 6)]


def func_3():
    return (i for i in range(10 ** 6))


start = time.time()  # фиксируем текущее время
func_1()  # вызываем функцию
result_1 = time.time() - start  # отнимаем текущее время от зафиксированного

start = time.time()
func_2()
result_2 = time.time() - start

start = time.time()
func_3()
result_3 = time.time() - start


print("Результат появится через")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)  # пауза 1 секунда


print(
    f"Время создания циклом: {result_1} с\n"
    f"Время создания конструктором: {result_2} с\n"
    f"Время создания генератором: {result_3} с\n"
)
