from blackjack import blackjack
from blackjack import clear


clear()

while True:
    
    play_game = input("Do you want to play a game of blackjack? Type'y' or 'n':\n").lower()
    if play_game == "y":
        blackjack()
    else:
        clear()
        break
    