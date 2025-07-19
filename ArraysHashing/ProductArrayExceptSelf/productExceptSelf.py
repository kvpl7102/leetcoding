class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n

        # Calculate prefix products
        prefix_product = 1
        for i in range(n):
            output[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products and combine with prefix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]

        return output
    
        

import unittest

class TestSolution(unittest.TestCase):
    def test_productExceptSelf(self):
        sol = Solution()

        # Test case 1: Basic example
        nums1 = [1, 2, 3, 4]
        expected1 = [24, 12, 8, 6]
        self.assertEqual(sol.productExceptSelf(nums1), expected1)

        # Test case 2: Contains zero
        nums2 = [-1, 1, 0, -3, 3]
        expected2 = [0, 0, 9, 0, 0]
        self.assertEqual(sol.productExceptSelf(nums2), expected2)

        # Test case 3: Single element (edge case)
        nums3 = [5]
        expected3 = [1]
        self.assertEqual(sol.productExceptSelf(nums3), expected3)

        # Test case 4: Two elements
        nums4 = [2, 3]
        expected4 = [3, 2]
        self.assertEqual(sol.productExceptSelf(nums4), expected4)

        # Test case 5: Negative numbers
        nums5 = [-1, -2, -3]
        expected5 = [6, 3, 2]
        self.assertEqual(sol.productExceptSelf(nums5), expected5)

        # Test case 6: All zeros (should handle correctly, product of others is 0)
        nums6 = [0, 0, 0]
        expected6 = [0, 0, 0]
        self.assertEqual(sol.productExceptSelf(nums6), expected6)

        # Test case 7: One zero, others non-zero
        nums7 = [1, 2, 0, 4]
        expected7 = [0, 0, 8, 0]
        self.assertEqual(sol.productExceptSelf(nums7), expected7)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)