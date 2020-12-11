import unittest
from ip_address import get_location


class TestIPAddress(unittest.TestCase):
    # IPTest: valid inputs
    def test_correct_values(self):
        # you should select some valid inputs, for which the output is known
        *other, location, city = get_location("153.138.24.18")
        self.assertEqual(location, "Japan")

    # invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        self.assertRaises(KeyError, lambda: get_location("20"))

    # corner case: empty string
    def test_empty_string(self):
        # you should input wrong data
        self.assertRaises(KeyError, lambda: get_location(" "))

if __name__ == '__main__':
    unittest.main()
