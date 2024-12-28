import unittest
from itertools import permutations

def generate_permutations(iterable, r=None):
    """
    Generate all permutations of a given iterable with an optional length 'r'.
    
    :param iterable: The iterable to permute
    :param r: The length of each permutation. If None, generates all full-length permutations.
    :return: A list of permutations
    """
    return list(permutations(iterable, r))

class TestGeneratePermutations(unittest.TestCase):
    
    def test_full_permutations(self):
        """Test full-length permutations of [1, 2, 3]."""
        expected = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
        result = generate_permutations([1, 2, 3])
        self.assertEqual(result, expected)
    
    def test_permutations_of_length_2(self):
        """Test permutations of length 2 from [1, 2, 3]."""
        expected = [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
        result = generate_permutations([1, 2, 3], 2)
        self.assertEqual(result, expected)

    def test_empty_list(self):
        """Test permutations of an empty list."""
        expected = [()]
        result = generate_permutations([])
        self.assertEqual(result, expected)

    def test_permutations_with_duplicates(self):
        """Test permutations of a list with duplicate elements."""
        expected = [(1, 1), (1, 1)]
        result = generate_permutations([1, 1])
        self.assertEqual(result, expected)

    def test_single_element(self):
        """Test permutations of a single-element list."""
        expected = [(1,)]
        result = generate_permutations([1])
        self.assertEqual(result, expected)


# Example usage
if __name__ == "__main__":
    unittest.main()
