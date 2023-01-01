"""
    Найти факториал числа n.

    !0 = 1
    !1 = 1

    !4 = 1 * 2 * 3 * 4 = 24

    !4 = 4 * 3 * 2 * 1 = 24
"""

number = int(input("Введите число: "))

factorial = 1
while number > 1:
    factorial *= number
    number -= 1

print(factorial)

# процесс вычисления для !4
# 4 -> 1 * 4 == 4
# 3 -> 4 * 3 == 12
# 2 -> 12 * 2 == 24
# factorial == 24
