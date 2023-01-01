def main():
    choice = input(
        "Меню: \n"
        "1. Найти количество четных и нечетных цифр числа.\n"
        "2. Найти факториал числа.\n"
        "3. Вывести последовательность чисел в степени до предела.\n"
        "4. Выход.\n"
        "Сделайте выбор и нажмите Enter: "
    )
    if choice == "1":
        odd_even()
    elif choice == "2":
        factorial()
    elif choice == "3":
        pow_limit()
    elif choice == "4":
        print("Bye!")
        return

    return main()


def odd_even():
    number = int(input("Ведите число: "))
    tmp = number
    even = 0
    odd = 0

    while number > 0:
        last_digit = number % 10

        if last_digit % 2 == 0:
            even += 1
        else:
            odd += 1

        number //= 10

    print("В числе", tmp, "четных цифр -", even, ", нечетных -", odd)


def factorial():
    number = int(input("Введите число, факториал которого найти: "))
    tmp = number
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    print("!", tmp, " = ", factorial, sep="")


def pow_limit():
    p = int(input("Введите степень: "))
    limit = int(input("Предел: "))
    number = 1

    while (result := number ** p) <= limit:
        print(result, end=" ")
        number += 1
    print()


if __name__ == '__main__':
    main()
