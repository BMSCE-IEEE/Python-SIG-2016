# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# File written after the test to implement the password generator
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE

# This is a short script to count and print the number of words in words.txt
# They are stored in a dictionary based on their length

# words.txt has each word on a newline
# words_2.txt has all the words on a single line separated by a space

# uncomment as required
word_file = open("words.txt", 'r')  # for words.txt
#word_file = open("words_2.txt", 'r')  # for words_2.txt

word_list = word_file.read().splitlines() # for words.txt
#word_list = word_file.readline().split(" ") # for words_2.txt

word_file.close()
word_dict = {}
for word in word_list:
    try:
        word_dict[len(word)] += 1
    except KeyError:
        word_dict[len(word)] = 1
print(word_dict)
print("total:", sum(word_dict.values()))
