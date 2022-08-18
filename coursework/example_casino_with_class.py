import json
from Player import Player
from MagicNum import MagicNum
from BlackJack import BlackJack


class Casino:

    def __init__(self):

        self.players_list = []
        self.create_players()
        try:
            with open('player_data.json') as file:
                pass
        except FileNotFoundError:
            with open('player_data.json', 'w') as file:
                json.dump({}, file, indent=4)

    def create_players(self):
        name = input(f'Введите Ваше имя: ').capitalize()
        self.players_list.append(Player(name))
        a = input('Есть ещё желающие играть? y/N: ')
        if a == 'y' or a == 'Y':
            self.create_players()

    def launch(self):
        """ Запуск игры. Авторизация и переход в главное меню. """
        self.main_menu()

    def main_menu(self):
        """ Отображение главного меню, запуск выбраных пунктов (методов). """
        choice = input(f"_____Menu_____\n"
                       f"Выберите игру:\n"
                       f"Magic Num: введи <1>\n"
                       f"Black Jack: введи <2>\n"
                       f"Для выхода: введите <0>\n")
        match choice:
            case '1':
                self.admin_magic_num()
            case '2':
                self.admin_blackjack()
            case '0':
                # names_gamer = ",".join(self.players_list)  # join не работает с методом __str__ объектов
                names_gamer = [pl.name for pl in self.players_list]
                names_gamer = ", ".join(names_gamer)
                print(f'\nПока {names_gamer}\n*********************\n\n')
                self.save_data_in_file()
            case _:
                self.main_menu()

    def admin_blackjack(self):
        while True:
            game = BlackJack(self.players_list)
            game.start_game()
            y_n = input('\n___________\nЕщё играем (Y/n)?')
            if y_n == 'n' or y_n == 'N':
                for pl in self.players_list:
                    print(f'\n******************************************\n'
                          f'{pl.name} твой профит со всех игр - {pl.get_data_blackjack()["profit"]}$\n')
                self.main_menu()
                break

    def admin_magic_num(self):
        if len(self.players_list) > 1:
            print('В игру Magic Num одновременно может играть только один человек. Будем играть по очереди :)')
            while True:
                for plyer in self.players_list:
                    print(f'\n___________________\nСЕЙЧАС ИГРАЕТ ИГРОК {plyer}')
                    game = MagicNum(plyer)
                    game.magic_num_game()
                winner = min(self.players_list, key=lambda pl: pl.attempt_num)
                print('\n**************************\n'
                      'В этой игре победил ', winner)
                y_n = input('\n___________\nЕщё играем (Y/n)?')
                if y_n == 'n' or y_n == 'N':
                    self.main_menu()
                    break
        else:
            while True:
                game = MagicNum(self.players_list[0])
                game.magic_num_game()
                y_n = input('Ещё играем (Y/n)?')
                if y_n == 'n' or y_n == 'N':
                    break
        self.main_menu()

    def save_data_in_file(self):
        with open('player_data.json', 'r+') as f:
            data: dict = json.load(f)
            # print(type(data), data)
            for pl in self.players_list:
                if pl.name in data.keys():
                    data[pl.name]['data_magic'] = pl.get_data_magic()
                    data[pl.name]['data_blackjack'] = pl.get_data_blackjack()
                else:
                    user_data: dict = {pl.name: {'data_magic': pl.get_data_magic(),
                                                 'data_blackjack': pl.get_data_blackjack()}
                                       }
                    data.update(user_data)
                print(f'Пользователь {pl} сохранен')
            f.seek(0)
            json.dump(data, f, indent=4)


def main():
    # Создаем объект класса Casino
    game = Casino()
    # Запускаем метод, который является точкой входа в игру
    game.launch()


if __name__ == "__main__":
    main()
