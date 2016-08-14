# Python SIG 2016 - Interview & Test to select Course Instructors for pySIG 2016
# 5th August, 2016
# BMS College of Engineering IEEE Student Branch, Bangalore
# https://github.com/BMSCE-IEEE

# Run this file to check if your implementation is working as expected.
# Use the -v flag for increased verbosity
# You can modify this code and check various test cases

import unittest
from order import *

class TestIsOrderedSubstring(unittest.TestCase):

    def setUp(self):
        pass

    def test_function(self):
        if is_ordered_substring('abc', 'a') is None:
            raise NotImplementedError("is_ordered_substring has not been implemented")
        self.assertTrue(is_ordered_substring('a Bcde$%#~~f', 'aBf'))
        self.assertTrue(is_ordered_substring('h123ello', 'hello'))
        self.assertFalse(is_ordered_substring('h         e   ll      o?<>:{}[]', 'hello123'))
        # len(check_order_string) can not be 0
        self.assertFalse(is_ordered_substring('abc', ''))


if __name__ == '__main__':
    unittest.main()
