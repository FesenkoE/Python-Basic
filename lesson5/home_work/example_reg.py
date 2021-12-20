"""
    Пример использования рекурсии для формы регистрации.

    Допустим программа задает вопрос: Сколько будет 2 + 2?
    до тех пор, пока не получит правильный ответ,
    после чего выводит сообщение "Верно, 4!".
"""


# def main():
#     answer = get_answer()
#     print(f'Верно: {answer}')
#
#
# def get_answer():
#     answer = input('Сколлько будет 2 + 2? ')
#
#     if answer == '4':
#         return answer
#     else:
#         return main()
#
#
# main()

"""
    Данную программу можно модифицировать, и для удобства пользователя
    выводить сообщение при неверном ответе.
"""


def main():
    answer = get_answer()
    print(f'Верно: {answer}')


def get_answer():
    answer = input('Сколлько будет 2 + 2? ')

    if answer != '4':
        print('Ответ неверный')
        return get_answer()

    return answer


main()
