# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE


# You have to implement a function selection_sort that takes a list of numbers
# as an argument and returns the sorted list. If you do not know
# the selection sort algorithm, refer the saved "Selection sort.html" Wikipedia page


def selection_sort(num_list):
    length = len(num_list)
    for i in range(0,l-1,1):        # Selects  the first item in the list
        min = num_list[i]           # and compares with the rest to find the minimum
        for j in range (i+1,l,1):
            if min > num_list[j]:
                min = num_list[j]
                pos = j
        if min != num_list[i]:              # If the selected number is not minimum,
            num_list[pos] = num_list[i]     # it is swapped with the minimum number
            num_list[i] = min
    return num_list
