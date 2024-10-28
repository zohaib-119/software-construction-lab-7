import unittest
from StringPermutations import generate_permutations
from StringPermutations import generate_permutations_unique

class TestPermutationFunctions(unittest.TestCase):
    
    def test_generate_permutations_distinct_characters(self):
        """Test basic input with distinct characters 'abc'."""
        self.assertEqual(sorted(generate_permutations("abc")), sorted(["abc", "acb", "bac", "bca", "cab", "cba"]),
                         "Should generate all permutations of 'abc'")

    def test_generate_permutations_two_characters(self):
        """Test input with two characters 'ab'."""
        self.assertEqual(sorted(generate_permutations("ab")), sorted(["ab", "ba"]),
                         "Should generate all permutations of 'ab'")

    def test_generate_permutations_single_character(self):
        """Test input with a single character 'a'."""
        self.assertEqual(generate_permutations("a"), ["a"],
                         "Should return ['a'] for a single character")

    def test_generate_permutations_three_distinct_characters(self):
        """Test input with three distinct characters 'xyz'."""
        self.assertEqual(sorted(generate_permutations("xyz")), sorted(["xyz", "xzy", "yxz", "yzx", "zxy", "zyx"]),
                         "Should generate all permutations of 'xyz'")

    def test_generate_permutations_empty_string(self):
        """Test input with an empty string."""
        self.assertEqual(generate_permutations(""), [""],
                         "Should return [''] for an empty string")

    def test_generate_permutations_unique_distinct_characters(self):
        """Test unique permutations of distinct characters 'abc'."""
        self.assertEqual(sorted(generate_permutations_unique("abc")), sorted(["abc", "acb", "bac", "bca", "cab", "cba"]),
                         "Should generate unique permutations of 'abc'")

    def test_generate_permutations_unique_two_characters(self):
        """Test unique permutations of two distinct characters 'ab'."""
        self.assertEqual(sorted(generate_permutations_unique("ab")), sorted(["ab", "ba"]),
                         "Should generate unique permutations of 'ab'")

    def test_generate_permutations_unique_duplicate_characters(self):
        """Test unique permutations of a string with duplicate characters 'aab'."""
        self.assertEqual(sorted(generate_permutations_unique("aab")), sorted(["aab", "aba", "baa"]),
                         "Should generate unique permutations of 'aab' with duplicates")

    def test_generate_permutations_unique_three_distinct_characters(self):
        """Test unique permutations of three distinct characters 'xyz'."""
        self.assertEqual(sorted(generate_permutations_unique("xyz")), sorted(["xyz", "xzy", "yxz", "yzx", "zxy", "zyx"]),
                         "Should generate unique permutations of 'xyz'")

    def test_generate_permutations_unique_empty_string(self):
        """Test unique permutations of an empty string."""
        self.assertEqual(generate_permutations_unique(""), [""],
                         "Should return [''] for an empty string")

if __name__ == "__main__":
    unittest.main()
