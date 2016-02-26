#!/usr/bin/env python
# -*- coding: utf-8 -*-
<<<<<<< HEAD
"""Task 03."""
=======
"""Tests Lesson 02 task 0333."""
>>>>>>> bf4afcea4e2cc6faba870eb8b9b78a9fdf46be11


# Import Python libs
import unittest


# Import user libs
import task_03


class Task03TestCase(unittest.TestCase):
<<<<<<< HEAD
    """Lesson 09, Task 03 tests"""

    def test_time_value(self):
        """Tests task_02.TIME value"""
        self.assertIs(task_03.JELLY, task_03.BUTTER)
=======
    """Task 03 tests"""

    def test_charlie(self):
        """Tests that CHARLIE has a value of 'Brown'"""
        self.assertEquals(task_03.CHARLIE, 'Brown')

    def test_violet(self):
        """Tests that VIOLET has a value of 'Gray'"""
        self.assertEquals(task_03.VIOLET, 'Gray')

    def test_patricia(self):
        """Tests that PATRICIA has a value of 'Reichardt'"""
        self.assertEquals(task_03.PATRICIA, 'Reichardt')

    def test_linus(self):
        """Tests that LINUS has a value of 'van Pelt'"""
        self.assertEquals(task_03.LINUS, 'van Pelt')
>>>>>>> bf4afcea4e2cc6faba870eb8b9b78a9fdf46be11


if __name__ == '__main__':
    unittest.main()
