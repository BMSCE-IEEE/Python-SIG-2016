# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE

# Your task is to create a password generator.
# First your password generator should ask the length of the password in characters.
# Then it should ask the number of passwords to generate.
# (Note that we may check large numbers like 100 to see if they are consistent and don't repeat)
# Should have an option to include uppercase alphabets or only use lowercase.
# Should have an option to include numbers or not.
# Should have an option to include non-alphanumeric symbols (like:"?!@#$") or not.
# Note that the password generated should be random and not form dictionary words.
# (HINT: Use the random module, check help(random))

# Bonus points: Making the password generator as user friendly as possible.

# Some suggestions: warns users when the password length is too short,
#                   generates passwords that are easy to remember but still secure (HINT: use words.txt)
#                   gives the passwords a strong / weak rating eg. from 1 to 5

import random, string
from math import log2
from datetime import datetime

wordfile = 'words.txt'
passwords_file = 'passwords.txt'

def main():
    """ Main function. Handles user input and calls generate_password or generate_random_password
        as required. Also displays passwords with ratings or writes them to passwords.txt
    """
    include_caps = None
    include_sym = None
    include_num = None
    # default value is False, generates random passwords
    word_based_password = False
    word_based_password = True if input("Password based on words.txt? y/N? ").lower() == 'y' else False
    if word_based_password:
        print("Generating passwords based on given words.txt")
    else:
        print("Expect totally (pseudo)random passwords!")
    try:
        Length = int(input('How long a password do you want? '))      # length of password
        if Length < 5:
            print('Password too small. Retry.')
            main()
            return 0
        elif Length < 8:
            print("Your password is not long enough to be safe. Consider a longer password.")
        elif Length < 12:
            print("Your password is long enough. (Hopefully.)")
        elif Length > 20 and word_based_password:
            print('Your password is too long, shorten it')
            main()
            return 0

        Number = int(input('How many passwords to generate? '))     # number of passwords
    except ValueError:
        print('Wrong input')
        main()
        return 0
    while (include_caps != 'yes' and include_caps != 'no'):
        include_caps = input('Do you want to include capital letters? yes/no: ').lower()    # option to include caps
    while (include_sym != 'yes' and include_sym != 'no'):
        include_sym = input('Do you want to include symbols? yes/no: ').lower()             # option to include symbols
    while (include_num != 'yes' and include_num != 'no'):
        include_num = input('Do you want to include numbers? yes/no: ').lower()             # option to include numbers
    write_to_file = False  # saves passwords to passwords.txt if True
    write_to_file = True if input("Save passwords to passwords.txt in current folder? y/N ").lower() == 'y' else False
    if write_to_file:
        print("\nSaving passwords to passwords.txt in current folder\n\n")
    else:
        print("\nDisplaying in terminal. Not saving passwords to passwords.txt\n\n")
    bool_dict = {'yes': True, 'no': False}

    if word_based_password:
        # generate (pseudo)random passwords based on words from words.txt
        passwords, word_ratings = generate_password(Length, Number, bool_dict[include_caps], bool_dict[include_sym], bool_dict[include_num])
    else:
        # totally pseudorandom passwords
        passwords = generate_random_password(Length, Number, bool_dict[include_caps], bool_dict[include_sym], bool_dict[include_num])
        word_ratings = None
    ratings = give_ratings(passwords, Length, bool_dict[include_caps], bool_dict[include_sym], bool_dict[include_num], word_ratings)

    if write_to_file:
        password_file = open(passwords_file, 'a')
        password_file.writelines(["\n\n", datetime.now().strftime('%Y-%m-%d %H:%M:%S     '), "\n\n"])
        password_file.writelines(["word_based_password: ", str(word_based_password), " Length: ", str(Length), " Number: ", str(Number), '\n'])
        password_file.writelines([str(passwords[i]) + "   Rating: " + str(round(ratings[i], 2)) + "\n" for i in range(len(passwords))])
        password_file.close()


    # display output
    for i in range(len(passwords)):
        print(passwords[i], round(ratings[i], 2), sep='   Rating: ')


def generate_password(Length, Number, include_caps_bool, include_sym_bool, include_num_bool):
    """ Generates list of passwords. Replaces with capitals, symbols and numbers
        depending on the Boolean input values.
    """
    passwords = []
    word_ratings = []
    sym_dict = {'a':'@', 'b':'8', 'c':'(', 'e':'3', 'h': '#', 'l':'!', 's':'$', 'o':'0'}
    # a dictionary used to replace the corresponding alphabets with symbols

    for i in range(Number):
        length = Length
        num_included = ''           # initializing the digits string included
        if include_num_bool:
            num = random.randint(1, int(Length / 4))
            # if numbers are to be included then reduce length to make space for numbers
            length = length - num
            num_included += "".join(random.sample(string.digits, num))
        string_list = list()
        string_list.append(num_included)
        word_found_bool = False
        while not word_found_bool:
            first_word_length = random.randint(2, length - 2)      # choose first word length
            if Length > 15:  # choose 3rd word also if length is higher than 15
                second_word_length = random.randint(2, length - (first_word_length))
                third_word_length = length - (first_word_length + second_word_length)
            else:
                second_word_length = length - first_word_length       # calculate second word length
                third_word_length = 0
            word_list, word_rating, word_found_bool = choose_words(first_word_length ,second_word_length, third_word_length)

        try:
            first_word, second_word, third_word = word_list
        except ValueError:
            first_word, second_word = word_list



        if include_caps_bool:
            # if capitals are to be included, randomly choose set of letters to be capitalised
            first_word_capitals = random.sample(first_word, (random.randint(1, int(first_word_length / 2) )))
            table = str.maketrans({item:item.upper() for item in first_word_capitals})
            first_word = first_word.translate(table)
            second_word_capitals = random.sample(second_word, (random.randint(1, int(second_word_length / 2) )))
            table = str.maketrans({item:item.upper() for item in second_word_capitals})
            second_word = second_word.translate(table)
            word_list = [first_word, second_word]
            try:
                third_word_capitals = random.sample(third_word, (random.randint(1, int(third_word_length / 2) )))
                table = str.maketrans({item:item.upper() for item in third_word_capitals})
                third_word = third_word.translate(table)
                word_list.append(third_word)
            except:
                pass
        string_list.extend(word_list)
        random.shuffle(string_list)
        password = "".join(string_list)
        word_ratings.append(word_rating)
        if include_sym_bool:
        # if symbols are to be included, replace alphabets according to predefined dictionary
            for sym in sym_dict.keys():
                if random.random() > .5:  # less than 1 / 2 chance of replacing with symbol
                    if sym in password:
                        password = password.replace(sym,sym_dict[sym])


        passwords.append(password)
    return passwords, word_ratings



def choose_words(first_word_length, second_word_length ,third_word_length):
    """ Chooses words of random length from words.txt to generate passwords.
        Calculates word rating from words.txt and probability.
    """
    first_words = []
    second_words = []
    third_words = []
    word_list = []
    word_found_bool = True
    fhand = open(wordfile)                         # wordfile has all the words
    wordlist = fhand.read().splitlines()  # for words.txt
    #wordlist = fhand.readline().split(" ")  # for words_2.txt
    fhand.close()
    for word in wordlist:
        if len(word) == first_word_length:          # check for lengths
            first_words.append(word)
        if len(word) == second_word_length:
            second_words.append(word)
        if third_word_length != 0 and len(word) == third_word_length:
            third_words.append(word)
    if len(first_words) == 0 or len(second_words) == 0 or (len(third_words) == 0 and third_word_length != 0):
        word_found_bool = False
        return None, None, word_found_bool
    first_word = random.choice(first_words).lower()         # choose words
    first_word_prob = 1 / len(first_words)
    second_word = random.choice(second_words).lower()
    second_word_prob = 1 / len(second_words)
    word_list.extend([first_word, second_word])
    if third_word_length != 0:
        third_word = random.choice(third_words).lower()
        third_word_prob = 1 / len(third_words)
        word_list.append(third_word)
    else:
        third_word_prob = 0
    word_rating = 1 - ((first_word_prob + second_word_prob + third_word_prob)/ (len(word_list)*3))
    return word_list, word_rating, word_found_bool


def generate_random_password(Length, Number, include_caps_bool, include_sym_bool, include_num_bool):
    """ Generates passwords pseudorandomly depending on Boolean input values.
    """
    valid_chars = string.ascii_lowercase   # initially only lowercase letters
    if include_caps_bool:
        valid_chars += string.ascii_uppercase
    if include_num_bool:
        valid_chars += string.digits
    if include_sym_bool:
        valid_chars += string.punctuation  # or only from sym dict ?
    # to use random.sample without ValueError if Length > len(valid_chars_list)
    valid_chars_list = list(valid_chars * ( int(Length / len(valid_chars)) + 1))
    passwords = list()  # empty list
    for i in range(Number):
        password = ''.join(random.sample(valid_chars_list, Length))
        passwords.append(password)
    return passwords


def give_ratings(passwords, Length, include_caps_bool, include_sym_bool, include_num_bool, word_ratings):
    """ Algorithm to rate the generated passwords. Takes word ratings from generate_password if password is word based.
        Try out your own and plot it with respect to various parameters with plot_password_ratings.py!
    """
    num_of_symbols = 26  # from string.ascii_lowercase
    if include_caps_bool:
        num_of_symbols += 26  # from string.ascii_uppercase
    if include_num_bool:
        num_of_symbols += 10  # from string.digits
    if include_sym_bool:
        num_of_symbols += 8  # '@', '8', '(', '3', '#', '!', '$', '0'

    entropy_per_bit = log2(num_of_symbols)
    basic_entropy = Length * entropy_per_bit
    max_entropy = 20 * log2(70)  # let a password of length 20 have maximum entropy
    if basic_entropy > max_entropy:
        basic_rating = 5.0
    else:
        basic_rating = (basic_entropy/max_entropy) * 5

    cap_sym_num_vals_list = []
    for password in passwords:
        cap_vals = 0
        sym_vals = 0
        num_vals = 0  # counts capitals, symbols and numbers in a password
        for char in password:
            if char in string.ascii_uppercase:
                cap_vals += 1
            elif char in string.digits:
                num_vals += 1
            elif char in '@8(3#!$0':
                sym_vals += 1
        # weighted avg of all caps, sym and nums
        cap_sym_num_vals = ((cap_vals + ( 2 * num_vals ) + ( 3 * sym_vals ) )* 3 )/ 6
        cap_sym_num_vals = (cap_sym_num_vals / len(password)) * 5  # ratio of cap_sym_num in password out of 5
        cap_sym_num_vals_list.append(cap_sym_num_vals)

    if word_ratings != None:
        ratings = []
        for i in range(len(word_ratings)):
            # Length / 4 gives 5/5 for a 20 character password
            # taking weighted average. Replace with your weights / algorithm and plot to see rating vs. length
            rating = ( 2.5 * basic_rating + (0.5 * (word_ratings[i] * 5)) + cap_sym_num_vals_list[i] + (Length / 4)) / 5
            ratings.append(rating)
        return ratings
    return [basic_rating for i in range(len(passwords))]




if __name__ == '__main__':
    main()
