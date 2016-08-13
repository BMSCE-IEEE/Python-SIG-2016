# Question:
You have to implement a game of Hangman. And if you don't know what that is,
have a look at Hangman.html ( EDIT: Since internet access wasn't allowed
in the exam, the saved HTML page was provided. Instead you can
have a look at https://en.wikipedia.org/wiki/Hangman_(game) )

The computer will have to choose a random word from words.txt
Let the maximum guesses allowed be 8
After every user guess,
The program should keep a track of guessed alphabets and print the available alphabets
Prints dashes unless alphabet has been guessed
When the word is correctly guessed, it calculates the score based on letter_score_dict
and the letters present in the word.
eg. 'bee' is (1 * score('b')) + (2 * score('e')) = 3 + 2 = 5
This score is added and a variable stores the user's total score over many games.
When there are no guesses left, the word is displayed and
10% of the word's score is subtracted from the user's score
After a word is played, the user enters either "exit" to quit the program or "again" to play again

Bonus points: Asking for username and keeping scores separately
              Implementing 2 player, where a player (not the computer) chooses the secret word
              Keeping track of the score even when the Python script is relaunched

letter_score_dict = \
{
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

 your code here
 (implement functions as required)
