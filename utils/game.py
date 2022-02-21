from typing import List

from player import Player, Deck



class Board:

    def __init__(self, players: List[str]):
        self.players = []
        for name in players:
            player = Player(name)
            self.players.append(player)
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def start_game(self):
        deck = Deck()
        deck.fill_deck()
        deck.distribute(self.players)
        while len(self.history_cards)<52-len(self.players):

            self.turn_count += 1
            self.history_cards += self.active_cards
            self.active_cards.clear()
            
            for player in self.players:

                card = player.play()
                if card != None:
                    self.active_cards.append(card)
                
            print(f"""
                Turn {self.turn_count}: {[card.value + card.icon for card in self.active_cards]} \n
                Cards played before this turn: {len(self.history_cards)}
                """)
            
            





