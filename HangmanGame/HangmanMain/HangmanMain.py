""" 
File:      HangmanMain.py 
Author:    Cody Christensen 
Date:      5/20/24 
Copyright: Cody Christensen - This work may not be copied for use in Academic Coursework. 
  
I, Cody Christensen, certify that I wrote this code  
from scratch and did not copy it in part or whole from another source. 
All references used in the completion of the assignments are cited  
in my README file. 

File Contents 
    This file contains all code necessary for a functioning hangman game. 
    The word to be guessed is generated using an imported random word generator, 
    and the user has ten guesses to correctly guess the word. The game can also be 
    replayed with a new word after completing a game. 
"""

from random_word import RandomWords

def generate_random_word():
    """
    Helper method used to produce and return a random word,
    where the whole word is in uppercase.

    Returns:
    str: Random word in uppercase
    """

    rand = RandomWords()
    word = rand.get_random_word()
    return word.upper()

def setup():
    """
    Used to setup some of the necessary data structures used
    in gameplay and obtain a random word, then starts gameplay
    by calling the gamePlay method.
    """

    guessing_placeholder = []

    # Get a random word and setup list containing the target word as well as a tracker list
    word_input = generate_random_word()
    input_word_array = list(word_input)
    tracker = list(word_input)

    # Fill up list that will be printed for guessing with underscores
    for i in range(len(input_word_array)):
        guessing_placeholder.append("_")

    # Start gameplay
    gamePlay(tracker, input_word_array, guessing_placeholder)


def gamePlay(tracker, input_word_array, guessing_placeholder):
    """
    Runs the actual gameplay, method is done and calls the endGame method
    when the incorrect guess limit is hit or the word has been correctly guessed.

    Parameters:
    tracker (list): List of chars representing the word to be guessed, used to track guessing progress
    input_word_array (list): List of chars representing the word to be guessed, used for referencing with guessed letters
    guessing_placeholder (list): List of chars representing the current letters guessed
    """

    word_guessed = False
    incorrect_guesses = 0
    already_guessed = []
    incorrect_letters = []

    while word_guessed == False:
        print(
            f"\n{' '.join(guessing_placeholder)}"
            + f"\nIncorrect guesses : {incorrect_guesses} / 10"
            + f"\nIncorrect letters : {' '.join(incorrect_letters)}"
            + "\nGuess a letter..."
        )

        guessed_letter = input().upper()

        # Check if entered letter has not already been guessed
        if not already_guessed.__contains__(guessed_letter):
            already_guessed.append(guessed_letter)

            # Check if word contains guessed letter
            if input_word_array.__contains__(guessed_letter):
                print("\nCorrect guess!")

                # Replace underscores with guessed letter
                for i in range(len(input_word_array)):
                    if input_word_array[i] == guessed_letter:
                        tracker.remove(guessed_letter)
                        guessing_placeholder[i] = guessed_letter

                # Check if full word has been guessed yet
                if tracker.__len__() == 0:
                    print(f"\nYou have guessed the word {''.join(input_word_array)}!")
                    word_guessed = True

            # When word does not contain guessed letter
            else:
                print("\nIncorrect guess!")
                incorrect_guesses += 1
                incorrect_letters.append(guessed_letter)

                # Check if user has hit incorrect guess limit
                if incorrect_guesses >= 10:
                    print("Game over!" + f"\nThe word was {''.join(input_word_array)}")
                    word_guessed = True

        # When user has already guessed that letter
        else:
            print("\n You already guessed that letter...")

    # When guess limit has been hit or word has been correctly guessed
    endGame()

def endGame():
    """
    Helper method called when game has ended, whether word has been
    guessed correctly or not.
    """

    print("\nWould you like to play another game? (Yes/No)")
    play_again = input().upper()
    
    if play_again == "YES":
        print("\nStarting new game...")
        setup()
    else:
        print("\nEnding game...")
        exit()

# Running code starts here, print welcome message and start setup
print("\nHello, welcome to hangman. You will have 10 guesses to correctly identify the word.")
setup()
