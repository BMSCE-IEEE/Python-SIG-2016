# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE


# You have to implement a function merge_sort that takes a list of numbers
# as an argument and returns the sorted list. If you do not know
# the merge sort algorithm, refer the saved "Merge sort.html" Wikipedia page


def merge_sort(num_list):
    
    if len(num_list) > 1:                   # If the length is one, its already sorted
        
        mid = len(num_list) // 2            # Decides the breaking point of list in half   
        left_half = num_list[:mid]          # Breaks the list into two halves    
        right_half = num_list[mid:]
        merge_sort(left_half)               # Using recursion, the list is repeatedly broken
        merge_sort(right_half)              # in halves until only one element in each is left
        left_index = 0
        right_index = 0                     
        sorted_index = 0
        while(i < len(left_half) and j < len(right_half)):
           if(left_half[i]>right_half[j]):
               num_list[k]=right_half[j]
               j+=1
           else:
               num_list[k] = left_half[i]
               i+=1
           k+=1

        while (i < len(left_half)):         # These loops sort the lists as they break and
            num_list[k] = left_half[i]      # overlaps the values in the original list
            i+=1
            k+=1
               
        while (j < len(right_half)):
            num_list[k] = right_half[j]
            j+=1
            k+=1
    return num_list
