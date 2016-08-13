# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE

# You have to implement a game of Hangman. And if you don't know what that is,
# have a look at Hangman.html ( EDIT: Since internet access wasn't allowed
# in the exam, the saved HTML page was provided. Instead you can
# have a look at https://en.wikipedia.org/wiki/Hangman_(game) )

# The computer will have to choose a random word from words.txt
# Let the maximum guesses allowed be 8
# After every user guess,
# The program should keep a track of guessed alphabets and print the available alphabets
# Prints dashes unless alphabet has been guessed
# When the word is correctly guessed, it calculates the score based on letter_score_dict
# and the letters present in the word.
# eg. 'bee' is (1 * score('b')) + (2 * score('e')) = 3 + 2 = 5
# This score is added and a variable stores the user's total score over many games.
# When there are no guesses left, the word is displayed and
# 10% of the word's score is subtracted from the user's score
# After a word is played, the user enters either "exit" to quit the program or "again" to play again

# Bonus points: Asking for username and keeping scores separately
#               Implementing 2 player, where a player (not the computer) chooses the secret word
#               Keeping track of the score even when the Python script is relaunched

letter_score_dict = \
{
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# your code here
# (implement functions as required)


# Contains default values for game configuration data
game_config_list = ["USERNAME", "SINGLE_PLAYER"]
total_score = 0  # total_score is a global variable referenced in update_score

import random, string, getpass
from datetime import datetime


def return_random_word():
    """ Reads words.txt and returns a random word.
        Assumes each word in words.txt is on a new line.
    """
    word_file = open("words.txt", 'r')
    word_list = word_file.read().splitlines()
    word_file.close()
    return random.choice(word_list)


def update_score(letter_score_dict, game_config_list, secret_word, word_guessed):
    """ Writes score and date to a textfile called USERNAME.txt (default) or specified username.
    """
    global total_score
    file_name = game_config_list[0] + ".txt"
    try:
        score_file = open(file_name, 'a')
    except:
        score_file = open(file_name, 'w')
    score = 0
    for char in secret_word.lower():
        score += letter_score_dict[char]
    if word_guessed:
        print("You guessed", secret_word)
        print("This is worth", score, "points!")
    else:
        score = score / 10; score = score * -1   # to deduct 10% of points
        print("You could not guess", secret_word)
        print("You lose", score * -1, "points!")  # to print positive value of score
    total_score += score
    print("Total score: ", total_score)
    score_file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S     '))
    score_file.write(str(score))
    score_file.write('\n')


def display_status(secret_word, guesses_left, guessed_list):
    """ Prints dashes and guessed letters. Returns True if secret_word has been guessed.
    """
    print() # print newline
    printed_dash = False
    for char in secret_word:
        if char in guessed_list:
            print(" ", char, "  ", end="")
        else:
            print(" __ ", end=""); printed_dash = True
    if not printed_dash:
        print("Congratulations!")
        return True
    else:
        print("      You have", guesses_left, "guesses left.")
        print()
        print("Remaining letters:")
        for char in string.ascii_uppercase:
            if char not in guessed_list:
                print(" ", char," ", end="")
        return False


def play_word_wrapper(letter_score_dict, game_config_list):
    """ Wrapper function for play_word.
        Checks if game mode is SINGLE_PLAYER or TWO_PLAYER,
        and sets the value of secret_word accordingly.
    """
    if game_config_list[1] == "TWO_PLAYER":
        secret_word = getpass.getpass("Player 1: Enter secret word:").upper()
        word_file = open("words.txt", 'r')
        word_list = word_file.read().splitlines()
        word_file.close()
        while secret_word.upper() not in word_list:
            print("That is not a valid English word according to words.txt")
            secret_word = getpass.getpass("Player 1: Enter secret word:").upper()
        print()  # to print newline
        if game_config_list[0] != "USERNAME":
            print(game_config_list[0], "  Start guessing!")
        elif game_config_list[0] == "USERNAME":
            print("Player 2: Start guessing!")
    elif game_config_list[1] == "SINGLE_PLAYER":
        # choose a random secret word from words.txt
        secret_word = return_random_word()
    play_word(letter_score_dict, game_config_list, secret_word)


def play_word(letter_score_dict, game_config_list, secret_word):
    """ Runs until 8 guesses are completed or a secret_word is guessed.
        Calls return_random_word, update_score and display_status as required.
    """
    guesses_left = 8
    guessed_list = []
    while guesses_left > 0:
        print()
        print()  # to print newline
        guess_letter = input("Enter your guess: ").upper()
        too_long = len(guess_letter) != 1
        not_letter = guess_letter not in string.ascii_uppercase
        already_guessed = guess_letter in guessed_list
        while (too_long or not_letter or already_guessed):
            guess_letter = input("Enter your guess: ").upper()
            too_long = len(guess_letter) != 1
            not_letter = guess_letter not in string.ascii_uppercase
            already_guessed = guess_letter in guessed_list
        guessed_list.append(guess_letter)
        valid_letter = guess_letter in secret_word
        if not valid_letter:
            guesses_left -= 1
        word_guessed = display_status(secret_word, guesses_left, guessed_list)
        if word_guessed:
            update_score(letter_score_dict, game_config_list, secret_word, True)
            break
    if guesses_left == 0:
        print("You ran out of guesses!")
        update_score(letter_score_dict, game_config_list, secret_word, False) # score -10%


def setup(letter_score_dict, game_config_list):
    """ Calls the function play_word_wrapper.
        Takes inputs 'again' and 'exit' and modifies game_config_list.
    """
    print("Welcome to hangman!")
    username = input("Enter username or 'skip': ")
    if username != "skip" and username != '':
        game_config_list[0] = username
        print("Setting username to: ", username)
    game_mode = input("Want to play against computer or 2 player? Choose '1' or '2'  ")
    while not (game_mode == '1' or game_mode == '2'):
        game_mode = input("Want to play against computer or 2 player? Choose '1' or '2'  ")
    if game_mode == '2':
        game_config_list[1] = "TWO_PLAYER"
    play_word_wrapper(letter_score_dict, game_config_list)
    while True:
        print()  # To print a newline.
        again_or_exit = input("Type 'again' to play again. 'exit' to exit the program.  ")
        while not (again_or_exit == 'again' or again_or_exit == 'exit'):
            again_or_exit = input("Type 'again' to play again. 'exit' to exit the program.  ")
        if again_or_exit == "again":
            play_word_wrapper(letter_score_dict, game_config_list)
        elif again_or_exit == "exit":
            print()
            print("You scored a total of", total_score, "points.")
            exit()


if __name__ == '__main__':
    setup(letter_score_dict, game_config_list)
