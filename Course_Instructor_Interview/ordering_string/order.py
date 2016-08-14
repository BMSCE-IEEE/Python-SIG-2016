# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE

# Function to remove all non-letters in input_string and store it in test_string
# Then check whether all characters in check_order_string are present in the
# same order in test_string

import string

def is_ordered_substring(input_string, check_order_string):
    test_string = ""
    for character in input_string:
        if character in string.ascii_letters:
            test_string += character

    # isPresent becomes true if check_order_string is within test_string
    is_present = False

	  # index holds the postion of the current character in test_string
    index = 0
    
    for character in check_order_string:
        is_present = True
        index = test_string[index:].find(character)
        
        if index == -1:
            is_present = False
            break
    
    return is_present   
