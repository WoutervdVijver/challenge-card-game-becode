from card import Card
from random import choice


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = [Card]
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = [Card]

    def play(self):
        self.turn_count += 1
        card = choice(self.cards)
        self.history.append(card)
        self.cards.remove(card)
        print(f"{self.name} on turn {self.turn_count} played: {card.value} of {card.icon}")
        return card