
class Diler:
    def __init__(self):
        self.point = 0
        self.cards = []

    def count_point_decorator(func):
        def wrapper(self, card):
            self.point += card.point
            if self.point > 21:
                for c in self.cards:
                    if c.meaning == 'Ace':
                        self.point -= 10
            result = func(self, card)
            return result
        return wrapper

    @count_point_decorator
    def get_card(self, card):
        self.cards.append(card)
