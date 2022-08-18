from Player import Player
import random


class MagicNum:

    def __init__(self, player):
        self.player = player
        self.__data_magic = player.get_data_magic()

    def print_result_magic_num(self):
        print(
            f'Результаты твоих игр в Magic num:\n'
            f'* пройдено игр: {self.__data_magic["games"]}\n'
            f'* рекорд: {self.__data_magic["record"]}\n'
            f'* средний результат: {self.__data_magic["avg_attempts"]}\n')

    def greeting_in_magic_num(self):
        if self.__data_magic['games'] == 0:
            print(f'Привет {self.player}!\n'
                  f'Это твоя первая игра!')
        else:
            self.print_result_magic_num()

        input('Поехали? Нажимай Enter')

    def magic_num_game(self):
        """
        """
        self.greeting_in_magic_num()
        count_attempt = 0
        rand = random.randint(0, 1000)
        while True:
            count_attempt += 1
            try:
                num = int(input(f'\n{count_attempt}. Введи число от 0 до 1000 : '))
            except ValueError:
                print('Твоё значение не число')
                continue
            if num < rand:
                print('Твоё значение меньше')
            elif num > rand:
                print('Твоё значение больше')
            else:
                print('\n__________\nВерно!', rand)
                print('Количество попыток:', count_attempt)
                _ = input('Жми Enter')
                break

        self.actualize_data_magic(count_attempt)

    def actualize_data_magic(self, count_attempt):
        if self.__data_magic['record'] == 999:
            self.__data_magic['record'] = count_attempt
        if self.__data_magic['record'] > count_attempt:
            self.__data_magic['record'] = count_attempt
            print('Это твой новый рекорд!!!')

        self.__data_magic['games'] += 1

        if self.__data_magic['avg_attempts'] == 999:
            self.__data_magic['avg_attempts'] = count_attempt
        else:
            new_attempts = (count_attempt + self.__data_magic['avg_attempts'] * (self.__data_magic['games'] - 1)) / \
                           self.__data_magic['games']
            self.__data_magic['avg_attempts'] = round(new_attempts, ndigits=3)
        self.player.set_data_magic(self.__data_magic)
        self.player.attempt_num = count_attempt

