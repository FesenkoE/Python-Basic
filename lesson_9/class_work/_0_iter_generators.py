"""
    Объекты, элементы которых можно перебирать в цикле for, содержат в себе
    объект итератор. Для того, чтобы его получить необходимо использовать
    функцию iter(), а для извлечения следующего элемента – функцию next().
"""


for i in range(5):
    print(i)


# создаем объект итератора из последовательности
a = iter(["one", "two", "three", "four", "five", "six"])
# a = iter(range(5))

print(next(a))  # получаем следующий элемент последовательности
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a, "end"))

big_iter = [i for i in range(10 ** 8)]  # конструктор списка

for i in big_iter:
    print(i)
    if i == 10:
        break

big_gen = (i for i in range(10 ** 8))  # генератор

for i in big_gen:
    print(i)
    if i == 10:
        break

print(next(big_gen))
print(next(big_gen))
print(next(big_gen))
print(next(big_gen))
print(next(big_gen))


# Создание функции-генератора
def even_range(start, end):
    current = start
    while current < end:
        yield current  # функция возвращает значение и фиксирует место выхода
        current += 2


for i in even_range(0, 10):
    print(i)


gen = even_range(0, 3)
print(next(gen))  # 0
print(next(gen))  # 2
