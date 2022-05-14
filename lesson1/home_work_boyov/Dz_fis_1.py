# # N1
# a = input('Ведите первое число: ')
# b = input('Ведите второе число: ')
# c = input('Ведите третье число: ')
# print(c)
# print(b)
# print(a)


# # N2
# a = input('Введите первое число: ')
# b = input('Введите второе число: ')
# c = input('Введите третье число: ')
# d = input('Введите четвертое число: ')
# result = (a + b) / (c + d)
# print(result)

# # N3
# name = input('Enter name: ')
# age = input('Enter age: ')
# city = input('Enter city: ')
# print(name, 'from', city)
# print('He is', age)

# # N4
# a = int(input('Ведите сторону прямоугольника: '))
# b = int(input('Ведите сторону прямоугольника: '))
# print("Периметр = ", (a + b) * 2)
# print("Площадь = ", a * b)

# N5
kat1 = int(input('Введите катет 1: '))
kat2 = int(input('Введите катет 2: '))

gipatenusa = (kat1 ** 2 + kat2 ** 2) ** 0.5

area = kat1 * kat2 / 2
perimeter = gipatenusa + kat1 + kat2

print('Площадь = ', area)
print('Периметр = ', perimeter)
