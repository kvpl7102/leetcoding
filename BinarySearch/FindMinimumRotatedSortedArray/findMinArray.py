import unittest
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        left, right = 0, n - 1

        
        return result
        

class TestFindMin(unittest.TestCase):

    def test_example_one(self):
        self.assertEqual(Solution().findMin([3,4,5,1,2]), 1)

    def test_example_two(self):
        self.assertEqual(Solution().findMin([4,5,6,7,0,1,2]), 0)

    def test_example_three(self):
        self.assertEqual(Solution().findMin([11,13,15,17]), 11)

    def test_single_element(self):
        self.assertEqual(Solution().findMin([1]), 1)

    def test_two_elements_rotated(self):
        self.assertEqual(Solution().findMin([2,1]), 1)

    def test_two_elements_sorted(self):
        self.assertEqual(Solution().findMin([1,2]), 1)

    def test_large_array(self):
        self.assertEqual(Solution().findMin([7,8,9,10,1,2,3,4,5,6]), 1)

    def test_another_large_array(self):
        self.assertEqual(Solution().findMin([5,1,2,3,4]), 1)

if __name__ == '__main__':
    unittest.main()
