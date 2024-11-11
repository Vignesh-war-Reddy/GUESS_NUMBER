from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Checks answer against guess and returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}.")
        return 0  # Game ends here, no turns left
    return turns - 1  # Reduce turns if guess is incorrect

# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while level not in ['easy', 'hard']:
        print("Invalid choice. Please choose 'easy' or 'hard'.")
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Function to validate user input (only accepts integers).
def valid_input(prompt):
    while True:
        try:
            guess = int(input(prompt))
            return guess
        except ValueError:
            print("Please enter a valid integer.")

# Ask user if they want to play again.
def play_again():
    return input("Do you want to play again? Type 'yes' or 'no': ").lower() == 'yes'

def game(debug=False):
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    if debug:
        print(f"Pssst, the correct answer is {answer}")
    
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = valid_input("Make a guess: ")

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
    
    if play_again():
        game(debug)

game(debug=False)
