from typing import List
from random import choice, shuffle

from card import Card


class Player:
    """
    A class to represent a player.

    Attributes
    ----------
    name: a str that represents the name of the player
    cards: a list of cards (as Card objects) that players is holding
    turn_count: int that keeps track of how many times turns a player took
    number_of_cards: number of cards the player is holding
    history: list of cards (as Card objects) that a player played.
    """

    def __init__(self, name):
        """
        :param name: str that represents name of player

        The following attibutes are initialized:
        name: as param name
        cards: empty list
        turn_count: int 0
        number_of_card: int  0
        history: empty list
        """
        self.name = name
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def play(self) -> Card:
        """
        Function that simulates player playing a card.

        :return: a randomly chosen card from attribute card and None if the player has no cards.

        the following attributes are updated:
        cards
        history

        """
        self.turn_count += 1
        if len(self.cards):
            card = choice(self.cards)
        else:
            print(f"{self.name} on turn {self.turn_count} has no cards")
            return None
        self.history.append(card)
        self.cards.remove(card)
        print(
            f"{self.name} on turn {self.turn_count} played: {card.value} of {card.icon}"
        )
        return card

    def receive_card(self, card: Card):
        """
        Function that adds a card to cards attribute
        
        :param card: card as Card class object
        """
        self.cards.append(card)
        self.number_of_cards += 1


class Deck:
    """
    The Deck class represents a standard deck of 52 playing cards.

    Attributes
    ----------
    deck: list of cards as Card objects
    """

    def __init__(self):
        """
        The following attibutes are initialized:
        deck: as empty list
        """
        self.deck = list([])

    def fill_deck(self):
        """
        Function that puts the 52 playing cards as Card objects in the deck attribute
        """
        self.deck.clear()
        for suit in ["♥", "♦", "♣", "♠"]:
            for value in [
                "A",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
            ]:
                card = Card(value, suit)
                self.deck.append(card)

    def shuffle(self):
        """
        Function that shuffles the cards in the deck list attribute
        """
        shuffle(self.deck)

    def distribute(self, players: List):
        """
        Function that distributes the cards in the deck as evenly as possible into the card attributes of the players

        :param players: list of Player class objects
        """

        while self.deck:
            for person in players:
                if self.deck:
                    person.receive_card(self.deck.pop())
                else:
                    break
