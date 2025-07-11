import unittest

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in num_map:
                num_map[num] = i
            else:
                return [num_map[complement], i]
        return []

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self):
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_example_3(self):
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])

    def test_negative_numbers(self):
        self.assertEqual(self.solution.twoSum([-1, -3, 5, 90], 4), [0, 2])

    def test_zero(self):
        self.assertEqual(self.solution.twoSum([0, 4, 3, 0], 0), [0, 3])

if __name__ == '__main__':
    unittest.main()
