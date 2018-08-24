import unittest
import numpy as np

import FileName

class TestFileName(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.x = np.zeros((3,3))

    def test_method1(self):
        """

        :return:
        """


    def test_method2(self):
    	"""

    	"""


    def tearDown(self):
        print("tearDown")
        del self.x


if __name__ == '__main__':
	"""
		test command: python -m unittest test_this_file.py
	"""
    unittest.main()