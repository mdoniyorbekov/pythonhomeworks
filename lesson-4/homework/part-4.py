import random

def number_guessing_game():
    while True:
        number = random.randint(1, 100)
        attempts = 10
        while attempts > 0:
            guess = int(input("Guess a number (1-100): "))
            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("You guessed it right!")
                break
            attempts -= 1
            print(f"Attempts left: {attempts}")
        if attempts == 0:
            play_again = input("You lost. Want to play again? ").lower()
            if play_again not in ['y', 'yes', 'ok']:
                break
        else:
            break
number_guessing_game()