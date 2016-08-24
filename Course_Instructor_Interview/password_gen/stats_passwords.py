# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE

# File written later to implement the password generator


# While making the password generator, the toughest part was thinking of a
# good algorithm to rate the passwords from 1 to 5
# This script generates 50 (default value of "number") passwords for every input combination
# and saves their average rating for lengths ranging from 5 to 20
# This is written to a file called passwords_data.txt
# Replace your algorithm (in password_generator) and use this file to generate passwords for all possible combinations
# After that, run plot_password_ratings.py to get graphs.

from password_generator import *


def main():
    passwords_data_file = 'passwords_data.txt'
    number = 50  # 50 passwords for every possible combination (ratings are then averaged)
    bool_list = [True, False]
    password_file = open(passwords_data_file, 'w')  # 'w' so that file is file is overwritten for everytime we plot_password_ratings
    print("Generating ", number," passwords for:")
    for word_based_password in bool_list:
        for include_caps in bool_list:
            for include_sym in bool_list:
                for include_num in bool_list:
                    print("word_based_password: ", word_based_password, " include_caps: ", include_caps, " include_sym: ", include_sym, " include_num: ", include_num)
                    print("Working...", end='', flush=True)
                    password_file.writelines(["\n\n# word_based_password: ", str(word_based_password)])
                    password_file.writelines([" Include_caps: " + str(include_caps)+ " Include_sym: " + str(include_sym)+ " Include_num: " + str(include_num)])
                    password_file.writelines(["\n# Time:", datetime.now().strftime('%Y-%m-%d %H:%M:%S '), "    Samples: ", str(number), "   "])
                    max_length = 20  # maximum supported length for word based password is 20
                    min_length = 5  # should be at least 5
                    for length in range(min_length, max_length+1):
                        if word_based_password:
                            passwords, word_ratings = generate_password(length, number, include_caps, include_sym, include_num)
                        else:
                            passwords = generate_random_password(length, number, include_caps, include_sym, include_num)
                            word_ratings = None
                        ratings = give_ratings(passwords, length, include_caps, include_sym, include_num,word_ratings)
                        password_file.writelines(["\n" + str(length) + " " + str(sum(ratings) / len(ratings))])
                        # sum / len gives average rating of "number" number of passwords for given options
                    print("Done.\n\n")
    password_file.close()
    print("Calculated average ratings for passwords with lengths from ", min_length, " to ", max_length, " for ", number, " samples.")
    print("Check ", passwords_data_file)

if __name__ == '__main__':
    main()
