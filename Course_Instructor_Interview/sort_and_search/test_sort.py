# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE


# Run this file to check if your implementation of a sorting algorithm
# is returning a sorted output. Use the -v flag for increased verbosity
# The actual algorithm will have to be verified manually.
# But with this you can find if it is working for a number of testcases.

import unittest
import random
from merge_sort import *
from selection_sort import *
from binary_search import *

class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_merge_sort(self):
        # can not use range() for Python 3 compatibility
        self.assertEqual(merge_sort([2,3,1]), [1,2,3])
        self.assertEqual(merge_sort(([3,5,6,7,2,1,0,4,8,9])), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_selection_sort(self):
        self.assertEqual(selection_sort([2,3,1]), [1,2,3])
        self.assertEqual(selection_sort(([3,5,6,7,2,1,0,4,8,9])), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_binary_search(self):
        self.assertFalse(binary_search([1,2,3], 4))
        self.assertTrue(binary_search([1,2,3], 1))



if __name__ == '__main__':
    unittest.main()
