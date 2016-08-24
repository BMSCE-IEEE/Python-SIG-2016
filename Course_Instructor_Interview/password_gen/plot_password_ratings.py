# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE

# File written later to implement the password generator


# While making the password generator, the toughest part was thinking of a
# good algorithm to rate the passwords from 1 to 5.
# So this script was made to help visualize how various parameters affect the rating
# Run this file after stats_passwords.py
# This file generates graphs as outputs. Requires matplotlib.

import matplotlib.pyplot as plt
import os

def read_data_from_file(word_based_password, include_caps, include_sym, include_num):
    """ Reads data from passwords_data.txt (which is saved by running stats_passwords.py)
        Extracts required data depending on user input and returns data_list to plot using matplotlib.
    """
    data_list = []; bool_dict = {'True': True, 'False': False}
    data_file = "passwords_data.txt"
    # checks if data_file exists and is not empty (run stats_passwords.py first)
    if os.path.exists(data_file) and os.path.getsize(data_file) > 0:
        with open("passwords_data.txt") as data_file:
            bool_list = []
            for line in data_file:
                if line.startswith("# word_based_password"):
                    bool_list = []  # stores conditions of a set of passwords (inputs to password generating function)
                    for element in line.split():
                        if element == 'True' or element == 'False':
                            bool_list.append(bool_dict[element])
                elif [word_based_password, include_caps, include_sym, include_num] == bool_list:
                    if line == '\n':
                        break  # required data has been stored, stop reading file
                    print(line)
                    data_list.append(line.strip('\n'))
    else:
        print("\n\n", data_file, " does not exist or is empty. Did you run stats_passwords.py before running this file?")
        exit()
    return data_list

include_caps = None
include_sym = None
include_num = None
# default value is False, generates random passwords
word_based_password = False
word_based_password = True if input("Plot passwords based on words.txt? y/N? ").lower() == 'y' else False
include_caps = True if input("Plot passwords with capitals? y/N? ").lower() == 'y' else False
include_num = True if input("Plot passwords with numbers? y/N? ").lower() == 'y' else False
include_sym = True if input("Plot passwords with symbols? y/N? ").lower() == 'y' else False
print("word_based_password: ", word_based_password)
print("include_caps: ", include_caps)
print("include_num: ", include_num)
print("include_sym: ", include_sym)
data_list = []
data_list = read_data_from_file(word_based_password, include_caps, include_sym, include_num)
# time, samples and other Boolean values in data_list[0]
data_list[0] = data_list[0] + "  word_based_password: " + str(word_based_password) + " include_caps: " + str(include_caps) + " include_num: " + str(include_num) + " include_sym: " + str(include_sym)
x_vals = [line.split()[0] for line in data_list[1:-1]]   # neglecting time, samples and Booleans (data_list[0])
y_vals = [line.split()[1] for line in data_list[1:-1]]   # data_list[-1] is ''
graph = plt.figure()
ax1 = graph.add_subplot(111)
plt.ylim((1, 5))  # ratings on Y axis go from 1 to 5
ax1.set_title(data_list[0])
ax1.set_xlabel('Length of password')
ax1.set_ylabel('Rating of password')
ax1.plot(x_vals,y_vals, c='r')
plt.show()
