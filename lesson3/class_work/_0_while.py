"""
    Цикл while.
    Тело цикло выполняется до тех пор, пока выполняется условие.

    while условие:
        выполняемый код

    После каждого прохода тела цикла (итерация) условие снова проверяется.
"""

number = 1

while number < 5:
    print(number)
    number += 1

while True:
    if number == 10:
        break  # завершает работу цикла

    if number % 2 == 0:
        number += 1
        continue  # прерывает текущую итерацию

    print(number)
    number += 1

print("out of while")
