from typing import List

from player import Player, Deck


class Board:
    """
    This class simulates a number of players playing a game.

    Attributes
    ----------
    players: list of players as Players objects
    turn_count: int to represent the current turn of game
    active_cards: list of Card class objects representing the cards played in this turn
    history_cars: list of Card class objects representing cards played in previous turns this turn excluding
    """

    def __init__(self, players: List[str]):
        """
        Function that initializes Board class objects

        :param player: list of strings of player names

        :initializes:
        players: a list of Player class objects with the given names from param player
        turn_count: int 0
        active_cards: empty list
        history_cards: empty list

        """
        self.player_names = players
        self.players = []
        for name in self.player_names:
            player = Player(name)
            self.players.append(player)
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def __str__(self) -> str:
        players_string = ""
        for name in self.player_names:
            players_string += str(name) + ", "
        players_string = players_string.rstrip(", ")
        active_card_string = ""
        for card in self.active_cards:
            active_card_string += card.value + card.icon + " "
        history_string = ""
        for card in self.history_cards:
            history_string += card.value + card.icon + " "
        return f"""
                These are the players of this game: {players_string}.\n
                During turn {self.turn_count}: \n
                These are the cards currently active {active_card_string} \n
                These are the cards previously active {history_string}
                """

    def start_game(self):
        """
        Function that simulates the playing of a game.
        First a deck is made, filled, shuffled and distributed.
        Next each player plays cards until no cards are left.
        After each turn the state of the game is printed.
        """
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)
        while len(self.history_cards) < 52 - len(self.players):

            self.turn_count += 1
            self.history_cards += self.active_cards
            self.active_cards.clear()

            for player in self.players:

                card = player.play()
                if card != None:
                    self.active_cards.append(card)

            print(
                f"""
                Turn {self.turn_count}: {[card.value + card.icon for card in self.active_cards]} \n
                Cards played before this turn: {len(self.history_cards)}
                """
            )
