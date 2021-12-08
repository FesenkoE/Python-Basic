"""
    Операторы сравнения: >, <, >=, <=, ==, !=

    В результате сравнении объектов получаем True либо False
"""

a = 10
b = 20

print(a < b)  # True
print(a == b)  # False


"""
    Логические операторы: and (и), or (или), not (не)
"""

# Выражение с успользованием оператора and истинно только тогда,
# когда истинны все операнды.

print(1 < 2 and 2 < 3)  # True

print(1 < 2 and 2 < 3 and 3 > 4)  # False


# Выражение с успользованием оператора or истинно тогда,
# когда хоть один операнд - истина.

a = 10

print(a < 0 or a == 10)  # True

print(a == 0 or a + 2 < 3 or a > 1)  # True


# Оператор not (не) меняет булевое значение на противоположное

print(not False)  # True
print(not True)  # False

b = -10 * 2
c = 'python'

print(not b == 20 and b < 1)  # True
# not b == 20 (екв. b != 20) - True и b < 1 - True


"""
    Операторы is, is not

    Применяются с bool и NoneType
"""

active = True
deleted = False
status = None

print(active is False)  # False
print(deleted is not None)  # True
print(status is None)  # True

result = None

a = 20
b = 20
if a < b:
    result = 10
elif a == b:
    result = 0

if result is not None:  # если делать условие if result, тогда 0 не пройдет
    print(result)
