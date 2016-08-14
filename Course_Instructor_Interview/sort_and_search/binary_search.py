# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE


# Now that you have a sorted array, you can search it faster using binary search
# instead of linear search. If you don't know the algorithm, check the .html file
# The function takes a list of numbers num_list and an integer to find var as arguments
# It should return a boolean value which is True if var exists in num_list, False otherwise

from selection_sort import *
from merge_sort import *
import sys

def parse_input(num_list):
    '''This function returns a list of intergers.
    It takes a string of whitespace or comma seperated numbers as input.'''
    if num_list.find(' ')>0:
        num_list = num_list.split(' ')      # This condition splits the string into a list
    elif num_list.find(',')>0:
        num_list = num_list.split(',')
    else:
        print ("Wrong Input")
        sys.exit(1)
    for x in range(0,len(num_list),1):      # This loop converts the elements of the
        num_list[x]=int(num_list[x])        # list from characters to integers
    return num_list
    

def binary_search(num_list, var):
    found_bool = False
    merge_sort(num_list)                    # This function sorts the list based on the merge_sort algorithm
    low_index = 0
    high_index = len(num_list)-1
    while(low_index<=high_index):
        mid = (low_index + high_index) // 2
        if num_list[mid] == var:
            found_bool = True
            break
        elif num_list[mid] > var:           # means the 'var' might be in the upper half
            high_index = mid -1
            mid = (low_index + high_index) // 2
        elif num_list[mid] < var:           # means the 'var' might be in the lower half
            low_index = mid + 1
            mid = (low_index + high_index) // 2
    return found_bool

#num_list = parse_input(input())            # If uncommented, this line accepts an input of
                                            # numbers separated by space or comma as string
