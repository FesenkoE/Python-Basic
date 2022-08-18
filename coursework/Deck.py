from Const import SUIT, MEANING
import random


class Card:
    def __init__(self, meaning, suit):
        self.meaning = meaning
        self.suit = suit
        self.point = self.get_point(self.meaning)

    @staticmethod
    def get_point(meaning):
        if meaning == 'Ace':
            return 11
        elif str.isdigit(meaning):
            return int(meaning)
        else:
            return 10

    def face(self):
        return f'{self.meaning} {self.suit}'


class Deck:
    def __init__(self):
        self.deck = self.create_deck()
        random.shuffle(self.deck)


    @staticmethod
    def create_deck():
        deck_list = []
        for meaning in MEANING:
            for suit in SUIT:
                deck_list.append(Card(meaning, suit))
        return deck_list

    def get_card(self):
        card = self.deck.pop()
        return card

# deck = Deck()
# for card in deck.deck:
#     print(card.face(), '----', card.point)