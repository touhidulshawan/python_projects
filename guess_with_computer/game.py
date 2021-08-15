from random import randint


def guess_the_number(num):
    random_number = randint(1, num)
    guess = 0
    live = 3
    continue_game = True
    winner = False
    while guess != random_number and continue_game:
        guess = int(input(f"Please enter number between 1 and {num}: "))
        live -= 1

        if guess < random_number:
            print("Too Low!!")
        elif guess > random_number:
            print("Too High!!")
        else:
            print("Yaay!! You win")
            continue_game = False
            winner = True

        if live > 1 and winner == False:
            print(f"You have only {live} lives to play")
        elif live == 1 and winner == False:
            print(f"You have only {live} live to play")

        if winner == False and live < 1:
            print("Sorry!! You lost the game")
            continue_game = False

    play_again = input("Want to play again (y/n): ")

    if play_again.lower() == 'y':
        gen_random_number = randint(10, 100)
        return guess_the_number(gen_random_number)
    else:
        print("Thanks for playing the game :)")
        exit()


guess_the_number(15)
