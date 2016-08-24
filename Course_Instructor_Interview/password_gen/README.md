# Instructions

* password_generator.py is the main password generator. If you select save to file option,
it saves passwords in "passwords.txt" by default. (Sample passwords.txt is provided)
* stats_passwords.py calculates average rating of 50 passwords of all 16 types and saves to "passwords_data.txt" by default (passwords_data.txt for 50 samples is provided)
* After running stats_passwords.py, run plot_password_ratings.py to generate graph using matplotlib.
* You can change the rating algorithm in password_generator.py and plot graphs.
* This directory contains 2 text files containing words. "words.txt" is used in all programs by default.
* analyse_words_txt.py will give the number of words of different lengths in words.txt or words_2.txt (Depending on which line is commented out)

# Question

Your task is to create a password generator.
First your password generator should ask the length of the password in characters.
Then it should ask the number of passwords to generate.
Should have an options to:
* include uppercase alphabets or only use lowercase.
* include numbers or not.
* include non-alphanumeric symbols (like:"?!@#$") or not.

Note that the password generated should be random and not form dictionary words.

Bonus points: Making the password generator as user friendly as possible.
