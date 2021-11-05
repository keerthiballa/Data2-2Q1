import unittest
from quiz1 import fibonacci


class ConverterTest(unittest.TestCase):

    def test_fibonacci(self):
        test_cases = [
            (5, 5),
            (6, 8),
            (7, 13),
            (10, 55),
            (11, 89),
        ]

        for fib_in, expected in test_cases:
            with self.subTest(f"{fib_in} -> {expected}"):
                self.assertEqual(expected, fibonacci.fibonacci(fib_in))
