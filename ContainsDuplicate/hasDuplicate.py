import unittest
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
        """
        nums_count = {}
        hasDuplicate = False
        for num in nums:
            if num in nums_count.keys():
                nums_count[num] += 1
                hasDuplicate = True
            else:
                nums_count[num] = 1
        return hasDuplicate 


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_has_duplicate(self):
        self.assertEqual(self.solution.hasDuplicate([1, 2, 3, 1]), True, "Should be True for [1, 2, 3, 1]")

    def test_no_duplicate(self):
        self.assertEqual(self.solution.hasDuplicate([1, 2, 3, 4]), False, "Should be False for [1, 2, 3, 4]")

    def test_empty_list(self):
        self.assertEqual(self.solution.hasDuplicate([]), False, "Should be False for an empty list")

    def test_single_element(self):
        self.assertEqual(self.solution.hasDuplicate([1]), False, "Should be False for a single element list")

    def test_all_duplicates(self):
        self.assertEqual(self.solution.hasDuplicate([1, 1, 1, 1]), True, "Should be True for [1, 1, 1, 1]")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)