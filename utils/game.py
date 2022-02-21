from typing import List

from card import Card
from player import Player, Deck



class Board:

    def __init__(self, players: List[str]):
        self.players = List[Player]
        for name in players:
            self.players.append(Player(name))
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def start_game(self):
        deck = Deck()
        deck.fill_deck()
        deck.distribute(self.players)
        while deck:
            self.turn__count += 1
            self.history_cards += self.active_cards
            self.active_cards.clear()

            for player in self.players:
                card = player.play()
                self.active_cards.append(card)
                
            
            print(f"""
                Turn {self.turn_count}: {[card.value + card.icon for card in self.active_cards]} \n
                Cards played this game: {len(self.history_cards)}
                """)





