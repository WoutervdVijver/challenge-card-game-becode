from random import choice, shuffle

from card import Card

class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []#

    def play(self):
        self.turn_count += 1
        if len(self.cards):
            card = choice(self.cards)
        else:
            print(f"{self.name} on turn {self.turn_count} has no cards")
            return None
        self.history.append(card)
        self.cards.remove(card)
        print(f"{self.name} on turn {self.turn_count} played: {card.value} of {card.icon}")
        return card




class Deck:

    def __init__(self):
        self.deck = list([])
        

    def fill_deck(self):
        self.deck.clear()
        for suit in ["♥", "♦", "♣", "♠"]:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                card = Card(value, suit)
                self.deck.append(card)
    
    def shuffle(self):
        shuffle(self.deck)

    def distribute(self, players):

        while self.deck:
            for person in players:
                try:
                    person.cards.append(self.deck.pop())
                except:
                    continue


