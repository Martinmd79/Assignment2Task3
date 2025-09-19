import unittest
from assignment2 import split_alphabets


class TestSplitAlphabets(unittest.TestCase):

    def setUp(self):
        """Set up method to run before each test case"""
        # This runs before each test method
        # You can initialize any common data here if needed
        pass

    def test_case_1_mixed_characters(self):
        """Test Case 1: Mixed uppercase and lowercase with duplicates"""

        input_chars = ['C', 'a', 'b', 'Z', 'c', 'Z']
        expected_lowercase = ['a', 'b', 'c']
        expected_uppercase = ['C', 'Z']

        # Call the function
        actual_lowercase, actual_uppercase = split_alphabets(input_chars)

        # Assert the results
        self.assertEqual(actual_lowercase, expected_lowercase)
        self.assertEqual(actual_uppercase, expected_uppercase)

    def test_case_2_case_sensivity(self):
        """Test Case 2: Case sensitivity test"""
        input_chars = ['D', 'd']
        expected_lowercase = ['d']
        expected_uppercase = ['D']

        actual_lowercase, actual_uppercase = split_alphabets(input_chars)
        self.assertEqual(actual_lowercase, expected_lowercase)
        self.assertEqual(actual_uppercase, expected_uppercase)


if __name__ == '__main__':
    unittest.main(verbosity=2)
