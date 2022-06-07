"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 050 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.

    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""

while True:
    phone_number = input('Enter phone number: ')
    prepare_phone_number = ''

    for digit in phone_number:
        if digit.isdigit():
            prepare_phone_number += digit

    if len(prepare_phone_number) < 10:
        continue
    else:
        phone_number = '38' + prepare_phone_number[-10:]

    print(f'Phone Number: {phone_number}')
    break
