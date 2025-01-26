import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_first_number(self):
        self.assertEqual(fibonacci(1), 0)

    def test_second_number(self):
        self.assertEqual(fibonacci(2), 1)

    def test_third_number(self):
        self.assertEqual(fibonacci(3), 1)

    def test_fifth_number(self):
        self.assertEqual(fibonacci(5), 3)

    def test_tenth_number(self):
        self.assertEqual(fibonacci(10), 34)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci(-5)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            fibonacci(0)

if __name__ == "__main__":
    unittest.main()
