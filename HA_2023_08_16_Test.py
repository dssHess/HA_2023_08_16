import unittest

from HA_2023_08_16 import multi 

class TestMulti(unittest.TestCase):

    def test_multi_function(self):
        self.assertEqual(multi(1, 2), 2)
        self.assertEqual(multi(4, 7), 28)

    def test_multi_function_with_floats(self):#1232183
        self.assertAlmostEqual(multi(3.1, 2.1), 6.51)


if __name__ == "__main__":
    unittest.main()