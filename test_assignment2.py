import unittest
from assignment2 import split_alphabets


class TestSplitAlphabets(unittest.TestCase):

    def setUp(self):
        """Optional setup before each test case"""
        pass

    def test_case_1_sorting_verification(self):
        input_chars = ['x', 'C', 'a', 'Z', 'm', 'B']
        expected_lowercase = ['a', 'm', 'x']
        expected_uppercase = ['B', 'C', 'Z']

        actual_lowercase, actual_uppercase = split_alphabets(input_chars)
        self.assertEqual(actual_lowercase, expected_lowercase)
        self.assertEqual(actual_uppercase, expected_uppercase)

    def test_case_2_case_sensitivity(self):
        input_chars = ['D', 'd']
        expected_lowercase = ['d']
        expected_uppercase = ['D']

        actual_lowercase, actual_uppercase = split_alphabets(input_chars)
        self.assertEqual(actual_lowercase, expected_lowercase)
        self.assertEqual(actual_uppercase, expected_uppercase)

    def test_case_3_only_lowercase(self):
        input_chars = ['b', 'm', 'a', 'w']
        expected_lowercase = ['a', 'b', 'm', 'w']
        expected_uppercase = []

        actual_lowercase, actual_uppercase = split_alphabets(input_chars)
        self.assertEqual(actual_lowercase, expected_lowercase)
        self.assertEqual(actual_uppercase, expected_uppercase)

    def test_case_4_only_uppercase(self):
        input_chars = ['Z', 'A', 'N']
        expected_lowercase = []
        expected_uppercase = ['A', 'N', 'Z']

        actual_lowercase, actual_uppercase = split_alphabets(input_chars)
        self.assertEqual(actual_lowercase, expected_lowercase)
        self.assertEqual(actual_uppercase, expected_uppercase)

    def test_case_5_maximum_boundary(self):
        input_chars = ['A', 'b', 'C', 'd', 'E', 'f', 'G', 'h', 'I', 'j',
                       'K', 'l', 'M', 'n', 'O', 'p', 'Q', 'r', 'S', 't']
        expected_lowercase = ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't']
        expected_uppercase = ['A', 'C', 'E', 'G', 'I', 'K', 'M', 'O', 'Q', 'S']

        actual_lowercase, actual_uppercase = split_alphabets(input_chars)
        self.assertEqual(actual_lowercase, expected_lowercase)
        self.assertEqual(actual_uppercase, expected_uppercase)

    def test_case_6_minimal_input(self):
        input_chars = ['z']
        expected_lowercase = ['z']
        expected_uppercase = []

        actual_lowercase, actual_uppercase = split_alphabets(input_chars)
        self.assertEqual(actual_lowercase, expected_lowercase)
        self.assertEqual(actual_uppercase, expected_uppercase)

    def test_case_7_identical_repetition(self):
        input_chars = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
        expected_lowercase = []
        expected_uppercase = ['B']

        actual_lowercase, actual_uppercase = split_alphabets(input_chars)
        self.assertEqual(actual_lowercase, expected_lowercase)
        self.assertEqual(actual_uppercase, expected_uppercase)


if __name__ == '__main__':
    unittest.main(verbosity=2)
