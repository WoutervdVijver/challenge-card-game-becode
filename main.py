from game import Board

# We first ask how many people want to play
number_of_players = int(input("how many players want to play? "))

# To avoid being stuck make sure number_of_players is not 0
while number_of_players == 0:
    number_of_players = int(
        input(
            """Nobody? Really? I don't believe you! \nHow many players want to play? """
        )
    )

# We ask the names of each player and if they are a bot
player_names = {}
for i in range(number_of_players):
    name = str(input(f"What is the name of player {i+1}?"))
    bot_or_not = str(input(f"Are you human and not a bot? y/n" ))
    player_names[name] = bot_or_not

# We run the game
board = Board(player_names)
board.start_game()
