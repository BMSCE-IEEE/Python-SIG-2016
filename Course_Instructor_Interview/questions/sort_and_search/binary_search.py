# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE


# Now that you have a sorted array, you can search it faster using binary search
# instead of linear search. If you don't know the algorithm, check the .html file
# ( EDIT: Since internet access wasn't allowed in the exam,
# the saved HTML page was provided. Instead you can
# have a look at https://en.wikipedia.org/wiki/Binary_search_algorithm )
# The arguments to the function are a list of numbers (num_list) and an integer to find (var)
# It should return a boolean value which is True if var exists in num_list, False otherwise

from selection_sort import *
from merge_sort import *

def parse_input():
    '''This function returns a list of intergers.
    It takes a string of whitespace or comma seperated numbers as input.'''

    # implement this function
    pass

def binary_search(num_list, var):
    found_bool = False
    # uncomment only one of these
    # selection_sort(num_list)
    # merge_sort(num_list)


    # implement this function
    return found_bool


# num_list = parse_input(input())
num_list = [1,2,3]
