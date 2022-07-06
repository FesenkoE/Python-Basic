"""
    Создать список, содержащий только целые числа (int) из списка а
"""

a = ["1", "3.14", "w", "one", "w3c", "123", "a"]

# 1 способ
b = []
for elem in a:
    if elem.isdigit():
        b.append(int(elem))

print(b)

# 2 способ

b = [int(elem) for elem in a if elem.isdigit()]

print(b)
