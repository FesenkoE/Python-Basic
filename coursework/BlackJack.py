from Deck import Deck
from Diler import Diler


class BlackJack:
    def __init__(self, pl_lst):
        self.deck = Deck()
        self.diler = Diler()
        self.players_list = pl_lst

    def accept_rate(self):
        print('\nИгра началась!'
              'Принимаются ставки от 10$ до 100$')
        for player in self.players_list:
            self.make_rate(player)

    def make_rate(self, player):
        try:
            rate = int(input(f'\n{player} СДЕЛАЙТЕ СТАВКУ: '))
            if 10 <= rate <= 100:
                player.make_rate(rate)
            else:
                print('Принимаются ставки от 10$ до 100$')
                return self.make_rate(player)
        except ValueError:
            return self.make_rate(player)

    def issue_cards(self):
        for player in self.players_list:
            self.get_card(player)
            print(f'\n'
                  f'{player.name}!'
                  f' Ваши карты:\n'
                  f'{player.cards[0].face()} и '
                  f'{player.cards[1].face()}')
        self.get_card(self.diler)
        print(f'\nВерхняя карта диллера:\n{self.diler.cards[0].face()}')

    def player_action(self):
        for player in self.players_list:
            action = input(f'\n____________________________\n'
                            f'{player.name}, ВАШИ ДЕЙСТВИЯ?\n'
                           f'1 - взять карту\n'
                           f'2 - пасс\n'
                           f'3 - слить игру\n')

            match action:
                case '1':
                    self.get_card(player)
                case '2':
                    pass
                case '3':
                    self.action_pass_game(player)
                case _:
                    pass

    def diler_action(self):
        print(f'Карты Дилера: {self.diler.cards[0].face()} и {self.diler.cards[1].face()}')
        if self.diler.point < 17:
            self.get_card(self.diler)

    def get_card(self, player):
        quantity_card = (2 if player.point == 0 else 1)
        if quantity_card > 1:
            for _ in range(quantity_card):
                player.get_card(self.deck.get_card())
        if quantity_card == 1:
            if type(player) is Diler:
                self.diler.get_card(self.deck.get_card())
                print(f'Дилер взял {self.diler.cards[-1].face()}')
                if self.diler.point < 17:
                    self.get_card(player)

            else:  # не дилер значит геймер
                player.get_card(self.deck.get_card())
                print(f'карта: {player.cards[-1].face()}\n'
                      f'уже собрано очков: {player.point}')
                i = input('ЕЩЁ?\n'
                          '1 - ещё\n'
                          '2 - хватит\n')
                if i == '1':
                    self.get_card(player)

    @staticmethod
    def action_pass_game(player):
        player.point = 0

    def game_summary(self):
        print(f'Дилер собрал {self.diler.point} очков')
        for pl in self.players_list:
            print(f'\n_-_-_-_-_-_-_-_-_-_-_-_-_\n{pl.name}, ты собрал {pl.point} очков')
            if pl.point == 0:
                pl.score -= pl.rate / 2
                print(f'Ты сдал карты и проиграл {pl.rate/2}$')
            elif self.check_blackjack(pl) and not self.check_blackjack(self.diler):
                pl.score += pl.rate * 1.5
                print(f'Поздравляю! BleckJack! Твой выигрыш {pl.rate * 1.5}$')
            elif 21 >= pl.point > self.diler.point or pl.point <= 21 < self.diler.point:
                pl.score += pl.rate
                print(f'Ты выиграл {pl.rate}$')
            elif pl.point > 21 and self.diler.point > 21 or pl.point == self.diler.point:
                print('Ничья, ты ничего не выиграл и ничего не проиграл')
            elif pl.point < self.diler.point <= 21:
                pl.score -= pl.rate
                print(f'Ты проиграл {pl.rate}$')
            elif pl.point > 21 >= self.diler.point:
                pl.score -= pl.rate
                print(f'Перебор! Ты проиграл {pl.rate}$')
            pl.set_data_blackjack()
            pl.zeroing_hand()

    def check_blackjack(self, pl):
        return pl.point == 21 and len(pl.cards) == 2

    def start_game(self):
        self.accept_rate()
        self.issue_cards()
        self.player_action()
        self.diler_action()
        self.game_summary()




