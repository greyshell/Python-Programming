#!/usr/bin/python
# author: greyshell

import unittest
from ds.sort import *


class TestSolution(unittest.TestCase):
    def test_counting_sort(self):
        """
        verify the correctness of the solution
        :return:
        """
        self.assertEquals(CustomSort.counting_sort([5, 40, 3, 260, 1], 1, 260),
                          [1, 3, 5, 40, 260])
        self.assertEquals(CustomSort.counting_sort([5, 2, 5, 1, 3, 2, 4], 1, 5),
                          [1, 2, 2, 3, 4, 5, 5])
        self.assertEquals(CustomSort.counting_sort([5, 40, 3, 270, 1], 1, 260),
                          None)


if __name__ == '__main__':
    unittest.main()
