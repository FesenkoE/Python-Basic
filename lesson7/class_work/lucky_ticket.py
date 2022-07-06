"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""

# Ниже описаны некоторые варианты решения задачи.


def is_lucky(ticket_num):
    # создадим список из цифр номера билета
    digits = [int(i) for i in str(ticket_num)]
    center = len(digits) // 2
    # if len(digits) % 2 != 0:
    #     return False
    return sum(digits[:center]) == sum(digits[center:])


def is_lucky(ticket_num):
    x = len(str(ticket_num)) // 2
    a = str(ticket_num)[:x]
    b = str(ticket_num)[x:]
    return sum(map(int, a)) == sum(map(int, b))


def is_lucky(ticket_num):
    num_list = list(str(ticket_num))
    first_sum = None
    second_sum = None

    if len(num_list) % 2 == 0:
        half_list = len(num_list) // 2
        first_sum = sum(list(map(int, num_list[:half_list])))
        second_sum = sum(list(map(int, num_list[half_list:])))

        return first_sum == second_sum
    return False


def is_lucky(ticket):
    sum_left = 0
    sum_right = 0
    l = len(str(ticket))
    for i in range(l):
        if i < l // 2:
            sum_right += ticket // 10 ** i % 10
        else:
            sum_left += ticket // 10 ** i % 10

    return sum_left == sum_right


def is_lucky(ticket_num):
    ticket_num = list(str(ticket_num))
    center = len(ticket_num) // 2
    ticket_num_1 = ticket_num[:center]
    ticket_num_2 = ticket_num[center:]
    sum_1 = 0
    sum_2 = 0
    for i in ticket_num_1:
        i = int(i)
        sum_1 += i
    for i in ticket_num_2:
        i = int(i)
        sum_2 += i
    return sum_1 == sum_2


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True
# assert is_lucky(4799731) is False

print("All tests passed successfully!")
