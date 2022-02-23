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
        self.score = 0

    def choose_card(self) -> Card:
        """
        Function that randomly choose a card from cards attribute

        :return card from Card class and None if no cards in cards attribute left
        """
        if len(self.cards):
            return choice(self.cards)
        else:
            return None


    def play(self, card: Card) -> Card:
        """
        Function that simulates player playing a card.

        :param card as Card class object

        :return: a Card class object from attribute card

        the following attributes are updated:
        cards
        history
        number_of_cards

        """

        self.turn_count += 1
        if card:
            self.number_of_cards -= 1
            self.history.append(card)
            self.cards.remove(card)
            print(
            f"{self.name} on turn {self.turn_count} played: {card.value} of {card.icon}"
            )
            return card
        else:
            print(
            f"{self.name} on turn {self.turn_count} has no cards left"
            )

    def receive_card(self, card: Card):
        """
        Function that adds a card to cards attribute
        
        :param card: card as Card class object
        """
        self.cards.append(card)
        self.number_of_cards += 1

    def receive_score(self, score: int):
        """
        Function that adds score to player

        :param score: int
        """
        self.score += score



class RealPlayer(Player):
    """
    This class represents a player that can be controlled by the user
    This class inherits from the Player class
    """
    def __init__(self, name):
        super().__init__(name)

    def choose_card(self) -> Card:
        """
        Function that allows the user to pick a card from cards attribute

        :return: a Card class object
        """
        
        if not self.cards:
            return None
        
        #Print all cards from cards attribute
        for i in range(self.number_of_cards):
            print(f"{i}: {self.cards[i].value}{self.cards[i].icon}")

        # ask what card to play and return it
        choice = int(input("Give the number of the card you want to play:"))
        while  choice>=self.number_of_cards:
            choice = int(input("""This is not a valid choice!
                        Give the number of the card you want to play:"""))
        return self.cards[choice]







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

    def distribute(self, players: List[Player]):
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

