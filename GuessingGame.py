import random

if __name__ == "__main__":
    print("Welcome to GuessingGame v0.1")
    playAgain = input("Do you want to play a guessing game? (Y/N): ")
    while playAgain == "Y" or playAgain == "y":
        print("I am thinking of a number between 1 and 10.")
        computerNumber = str(random.randint(1,10))
        guess = input("Try to guess my number: ")
        while guess != computerNumber:
            guess = input("Wrong! Guess again: ")
        print("Yes! My number was " + computerNumber + "!")
        playAgain = input("Play again ? (Y/N): ")

