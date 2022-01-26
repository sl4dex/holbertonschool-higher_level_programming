#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ class to test max_integer function """
    def test_types(self):
        """ check if data types are correctly handled """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -80, 0]), 0)
        self.assertEqual(max_integer([4, 4, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4.5]), 4.5)
        self.assertEqual(max_integer([0.2, 0.5, 0.8, True]), 1)
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "h"])
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(
                         [1, 999991999999999919999999999123456789123456789]),
                         999991999999999919999999999123456789123456789)


if __name__ == '__main__':
    unittest.main()
