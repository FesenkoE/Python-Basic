# import abc
import json


class Player:
    def __init__(self, name):
        self.name = name
        self.__data_magic = None
        self.__data_blackjack = None
        self.login()
        self.attempt_num = None
        self.rate = None
        self.point = 0
        self.cards = []
        self.score = 0

    def __repr__(self):
        return self.name

    # def __str__(self):
    #     return self.name

    def login(self):
        """
        Авторизация и запись информации об игроке.

        Пользователь вводит имя (input), по имени с файла получаем его данные.
        Если данных по такому имени не существует, то создаем их.

        После получения/создания записываем в атрибут класса.
        """
        with open('player_data.json', 'r') as file:
            data: dict = json.load(file)
            if self.name in data.keys():
                self.__data_magic = data[self.name]['data_magic']
                self.__data_blackjack = data[self.name]['data_blackjack']
            else:
                self.__data_magic = {'games': 0, 'record': 999, 'avg_attempts': 999}
                self.__data_blackjack = {'games': 0, 'profit': 0}

    def make_rate(self, rate):
        self.rate = rate

    def count_point_decorator(func):
        def wrapper(self, card):
            self.point += card.point
            result = func(self, card)
            if self.point > 21:
                for c in self.cards:
                    if c.meaning == 'Ace':
                        c.meaning = "#Ace"
                        self.point -= 10
                        break
            return result
        return wrapper

    @count_point_decorator
    def get_card(self, card):
        self.cards.append(card)

    def get_data_magic(self):
        return self.__data_magic

    def get_data_blackjack(self):
        return self.__data_blackjack

    def set_data_magic(self, data_magic):
        self.__data_magic = data_magic

    def set_data_blackjack(self):
        self.__data_blackjack['profit'] += self.score
        self.__data_blackjack['games'] += 1

    def zeroing_hand(self):
        self.cards.clear()
        self.point = 0
        self.score = 0

    def __del__(self):
        """ При удалении обновляем информацию из атрибута в файле """
        print(f"Игрок {self.name} удален с памяти.")

    # def make_split(self):





