"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 050 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.

    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""

while True:
    phone = input('Enter phone number: ')

    digits = ''
    for char in phone:
        if char.isdigit():
            digits += char

    if len(digits) >= 9:
        phone = '380' + digits[-9:]
    else:
        print('Wrong format.')
        continue

    print(phone)

    if input('Continue? (y/n) ') != 'y':
        break

print('Bye!')
