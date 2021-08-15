from random import choice


def message():
    print("""
 Choose a option:
 r -> rock
 p -> paper
 s -> scissors
 """)


def play():
    message()
    player = input("Type your choice: ")
    computer = choice(['r', 'p', 's'])

    if player.lower() == computer:
        return print("It\'s a tie")

    if choose_winner(player, computer):
        return print("Hurray!! You win.")

    return print("Sorry!! You lost the game")


def choose_winner(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent ==
                                               "r") or (player == "s" and opponent == "p"):
        return True


play()
