"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num):
    sum_1 = sum_2 = 0
    ticket_num = str(ticket_num)

    if len(ticket_num) % 2 != 0:
        return False

    for digit in ticket_num[:int(len(ticket_num) / 2)]:
        sum_1 += int(digit)

    for digit in ticket_num[int(len(ticket_num) / 2):]:
        sum_2 += int(digit)

    return sum_1 == sum_2


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True
assert is_lucky(4799731) is False
#
print("All tests passed successfully!")
