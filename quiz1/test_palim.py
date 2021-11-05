import unittest
import quiz1.palindrome
from quiz1.palindrome import palindrome


class PalindromeTest(unittest.TestCase):

    def test_is_palindrome(self):
        test_cases = [
            ("redivider", True),
            ("deified", True),
            ("civic", True),
            ("radar", True),
            ("level", True),
            ("palindrome", False),
            ("Python", False)
        ]
        for str_in, expected in test_cases:
            with self.subTest(f"{str_in} -> {expected}"):
                self.assertEqual(expected, palindrome(str_in))