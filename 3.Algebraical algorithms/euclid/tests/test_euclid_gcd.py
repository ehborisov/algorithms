import unittest
from euclid import euclid_gcd
from parameterized import parameterized


class MyTestCase(unittest.TestCase):

    @parameterized.expand(
        [
            [None, 1, 1, 1],
            [None, 2, 2, 2],
            [None, 5, 1, 1],
            [None, 25, 10, 5],
            [None, 10, 25, 5],
            [None, 624129, 2061517, 18913],
            [None, 265252859812191058636308479999999, 19134702400093278081449423917, 1],
        ]
    )
    def test_gcd(self, _, a, b, expected):
        self.assertEqual(expected, euclid_gcd.gcd_subtraction(a, b), "GCD Subtraction algorithm error")
        self.assertEqual(expected, euclid_gcd.gcd_division(a, b), "GCD Division algorithm error")
        self.assertEqual(expected, euclid_gcd.gcd_bitwise(a, b), "GCD Bitwise algorithm error")


if __name__ == '__main__':
    unittest.main()
