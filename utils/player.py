from random import choice, shuffle
from typing import List

from card import Card

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





class Deck:

    def __init__(self):
        self.deck = []
        

    def fill_deck(self):
        self.deck.clear()
        for suit in ["♥", "♦", "♣", "♠"]:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.deck.append(Card(value, suit))
    
    def shuffle(self):
        self.deck = shuffle(self.deck)

    def distribute(self, players: List[Player]):

        while self.deck:
            for person in players:
                person.cards.append(self.deck.pop())

