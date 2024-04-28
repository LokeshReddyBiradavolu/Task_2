import random
import time

def get_name():
    print("May I ask you for your name?")
    return input()

def intro(name):
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def get_guess():
    while True:
        guess = input("Guess: ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 200:
                return guess
            else:
                print("Silly Goose! That number isn't in the range! Please enter a number between 1 and 200")
        else:
            print(f"I don't think that {guess} is a number. Sorry")

def play_game(name):
    number = random.randint(1, 200)
    guesses_taken = 0
    while guesses_taken < 6:
        guess = get_guess()
        guesses_taken += 1
        if guess < number:
            print("The guess of the number that you have entered is too low")
        elif guess > number:
            print("The guess of the number that you have entered is too high")
        else:
            print(f'Good job, {name}! You guessed my number in {guesses_taken} guesses!')
            return
        if guesses_taken < 6:
            time.sleep(0.5)
            print("Try Again!")
    print(f'Nope. The number I was thinking of was {number}')

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

def main():
    while True:
        name = get_name()
        intro(name)
        play_game(name)
        if not play_again():
            break

if __name__ == "__main__":
    main()
