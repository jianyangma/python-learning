"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    count = INITIAL_GUESSES
    length = len(secret_word)
    dashes = ""
    for i in range(length):
        dashes += "-"
    print("The word now looks like this: " + dashes)
    dashes = list(dashes)
    while True:
        print("You have " + str(count) + " guesses left")
        guess = input("Type a single letter here, then press enter: ")
        if len(guess) != 1:
            print("Guess should only be a single character.")
            result = ''.join(dashes)
            print("The word now looks like this: " + result)
            continue
        guess = guess.upper()
        if guess not in secret_word:
            print("There are no " + guess + "'s in the word")
            count -= 1
            if count == 0:
                print("Sorry, you lost. The secret word was: " + secret_word)
                break
        else:
            print("That guess is correct.")
            for i in range(length):
                if guess == secret_word[i]:
                    dashes[i] = guess
        result = ''.join(dashes)
        if result == secret_word:
            print("Congratulations, the word is: " + secret_word)
            break
        print("The word now looks like this: " + result)


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    test = []
    with open(LEXICON_FILE, 'r') as file:
        for word in file:
            word = word.strip()
            test.append(word)
    index = random.randrange(len(test))
    return test[index]


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
