from utils.game import Board

number_of_players = input("how many players want to play?")

player_names= []
for i in range(number_of_players):
    name = input(f"What is the name of player {i+1}")
    player_names.append(name)

board = Board(player_names)
board.start_game()

