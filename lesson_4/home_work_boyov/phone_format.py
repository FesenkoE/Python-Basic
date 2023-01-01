"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 050 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.

    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
    попросить пользователя повторить ввод.
"""
while True:
    phone_num = input('Enter phone number: ')
    for char in phone_num:
        if not char.isdigit():
            phone_num = phone_num.replace(char, '')  # удаляем лишние символы
    if len(phone_num) >= 9:
        phone_num = '380' + phone_num[-9::]

#    if phone_num[-10] == '0':  # ecли 10й символ с конца 0, значит колличество цифр верное
#       break
    else:
        print('Неверный формат')
        continue

    print(phone_num)

    if input('Continue? (Y/n) ') != 'y':
        break


