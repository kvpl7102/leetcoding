import collections

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                length = 0
                while (num + length) in nums:
                    length += 1
                longest = max(length, longest)

        return longest

import unittest

class TestLongestConsecutiveSequence(unittest.TestCase):

    def test_example_1(self):
        s = Solution()
        self.assertEqual(s.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_example_2(self):
        s = Solution()
        self.assertEqual(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_empty_array(self):
        s = Solution()
        self.assertEqual(s.longestConsecutive([]), 0)

    def test_single_element(self):
        s = Solution()
        self.assertEqual(s.longestConsecutive([1]), 1)

    def test_no_consecutive(self):
        s = Solution()
        self.assertEqual(s.longestConsecutive([1, 5, 9, 13]), 1)

    def test_duplicates(self):
        s = Solution()
        self.assertEqual(s.longestConsecutive([1, 2, 0, 1]), 3)

    def test_negative_numbers(self):
        s = Solution()
        self.assertEqual(s.longestConsecutive([-1, 0, 1, 2, 3]), 5)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)