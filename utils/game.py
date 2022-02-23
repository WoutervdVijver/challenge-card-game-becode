from typing import Dict, List

from player import Player, RealPlayer, Deck
from card import Card


class Board:
    """
    This class simulates a number of players playing a game.

    Attributes
    ----------
    players: list of players as Players objects
    turn_count: int to represent the current turn of game
    active_cards: list of Card class objects representing the cards played in this turn
    history_cars: list of Card class objects representing cards played in previous turns this turn excluding
    trump: defines a trump card for the game
    """

    def __init__(self, players: Dict[str, str]):
        """
        Function that initializes Board class objects

        :param player: list of strings of player names

        :initializes:
        players: a list of Player class objects with the given names from param player
        turn_count: int 0
        active_cards: empty list
        history_cards: empty list
        trump: str "SA"

        """
        self.player_names = players
        self.players = []
        for name in self.player_names.keys():
            if self.player_names[name] == 'y':
                player = RealPlayer(name)
            else:
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
        for card in self.active_cards.keys:
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
        After each turn the state of the game is printed.
        """
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)

        game_state = GameState("SA")


        while len(self.history_cards) < 52 - len(self.players):

            self.turn_count += 1
            self.history_cards += self.active_cards
            self.active_cards.clear()

            who_played_what = {}
            for player in self.players:

                card = player.play(player.choose_card())
                who_played_what[card] = player
                self.active_cards.append(card)

            winning_card = game_state.winning_card(self.active_cards)
            winning_player = who_played_what[winning_card]
            score = game_state.scorer(self.active_cards)
            winning_player.receive_score(score)


            print(
                f"""
                Turn {self.turn_count}: {[card.value + card.icon for card in self.active_cards]} \n
                Cards played before this turn: {len(self.history_cards)} \n
                """
            )
            print("Scores of the players: ")
            for player in self.players:
                print(f"{player.name}: {str(player.score)}")
            print(" ")

            if winning_player.score>10:
                print(f"""
                {winning_player.name} won the game!"
                """)
                break
          
    
            
    

class GameState:
    """
    This class represents the specific game that will be played

    Attributes
    ----------

    trump: str representing the trump suit of this game
    game_value: a dictionary giving a game value for each card value
    scores: a dictionary giving a score for each card value
    """
    def __init__(self, trump):
        self.trump = trump
        self.game_value = {'A': 13,
                        'K':12,
                        'Q': 11,
                        'J': 10,
                        '10': 9,
                        '9': 8,
                        '8': 7,
                        '7': 6,
                        '6': 5,
                        '5': 4,
                        '4': 3,
                        '3': 2,
                        '2': 1,
        }

        self.scores = {'A': 5,
                        'K':4,
                        'Q': 3,
                        'J': 2,
                        '10': 1,
                        '9': 0,
                        '8': 0,
                        '7': 0,
                        '6': 0,
                        '5': 0,
                        '4': 0,
                        '3': 0,
                        '2': 0,
        }

    def winning_card(self, list_of_cards: List[Card]) -> Card:
        """
         Function that given a list of cards returns the winning card

         :params list_of cards: 

         :return: Card
        """
        winning_card = list_of_cards[0]
        for card in list_of_cards:
            if winning_card.icon!=self.trump and card.icon!=self.trump:
                if self.game_value[winning_card.value] < self.game_value[card.value]:
                    winning_card = card
            elif winning_card.icon!=self.trump and card.icon==self.trump:
                winning_card = card
            elif winning_card.icon==self.trump and card.icon==self.trump:
                if self.game_value[winning_card.value] < self.game_value[card.value]:
                    winning_card = card
        
        return winning_card 

    def scorer(self, list_of_cards: List[Card]) -> int:
        """
        Function that scores a list of cards

        :params list_of_cards as a list of Card objects

        :returns score as int
        """
        score = 0
        for card in list_of_cards:
            score += self.scores[card.value]
        return score
