"""
Test helper functions
"""

import unittest
from sample import find_sum

class TestSampleMethods(unittest.TestCase):
    """
    Test harness
    """

    def test_find_sum(self):
        """
        Test sums
        """
        self.assertEqual(find_sum(3), 6)
        self.assertEqual(find_sum(10), 55)


if __name__ == '__main__':
    unittest.main()
