from asyncio import Handle
from mimetypes import guess_all_extensions
from random import randint
from art import logo

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

# function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns -1
        """return used here because turn-=1(means to perform operations on global variabal is not a good idea.)"""
        """but we can do turn-=1 too."""
    elif guess < answer:
        print("Too low.")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}.")

# Make function to set diificulty.
def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Choosing a random number between 1 and 100.

    answer = randint(1,100)
    print(f"Pssst,the correct answer is {answer}")

    turns=set_difficulty()
    # Repeate the guessing functionality if they get it wrong.
    guess=0
    while guess != answer:
        # print()
        print(f'You have {turns} attempts remaining to guess the number.')
        # Let the user guesss the number.
        guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
      """here return is used to get out from the function.and to stop the loop..."""
    elif guess != answer:
      print("Guess again.")


game()

