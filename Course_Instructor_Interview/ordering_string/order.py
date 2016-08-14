# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE

# Function to remove all non-letters in input_string and store it in test_string
# Then check whether all characters in check_order_string are present in the
# same order in test_string

import string

def is_ordered_substring( input_string, check_order_string ):
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
        index = string.find( test_string[index:], character )
        
        if index == -1:
            is_present = False
            break
    
    return found   

def is_ordered_substring_wrapper():
    # Function to take input and call is_ordered_substring
    input_string = input( "Enter Input String: " )
    if input_string == "":
        input_string = input( "Enter Input String: " )
    
    order_string = input( "Enter Ordered String: " )
    if order_string == "":
        order_string = input( "Enter Ordered String: " )
    
    is_ordered = is_ordered_substring( input_string, order )
    if is_ordered:
        print( order_string, "is present in", input_string, "in the same order" )
    else:
        print( order_string, "is not present in", input_string, "in the same order" )

while True:    
    again_or_exit = input("Type 'again' to run again. 'exit' to exit the program.  ")
    while not (again_or_exit == 'again' or again_or_exit == 'exit'):
        again_or_exit = input("Type 'again' to run again. 'exit' to exit the program.  ")
    if again_or_exit == "again":
        is_ordered_substring_wrapper()
    elif again_or_exit == "exit":
        exit()
