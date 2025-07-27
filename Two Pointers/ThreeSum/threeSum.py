import unittest

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
    

class TestThreeSum(unittest.TestCase):
    def test_example_1(self):
        nums = [-1,0,1,2,-1,-4]
        expected = [[-1,-1,2],[-1,0,1]]
        result = Solution().threeSum(nums)
        result.sort()
        for triplet in result:
            triplet.sort()
        expected.sort()
        for triplet in expected:
            triplet.sort()
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [0,1,1]
        expected = []
        result = Solution().threeSum(nums)
        self.assertEqual(result, expected)

    def test_example_3(self):
        nums = [0,0,0]
        expected = [[0,0,0]]
        result = Solution().threeSum(nums)
        self.assertEqual(result, expected)

    def test_no_triplets(self):
        nums = [-2,-1,0,3,4]
        expected = []
        result = Solution().threeSum(nums)
        self.assertEqual(result, expected)

    def test_duplicates_and_zeros(self):
        nums = [-1,0,1,0,-1,2,-1,-4,-2]
        expected = [[-2,0,2],[-1,-1,2],[-1,0,1]]
        result = Solution().threeSum(nums)
        result.sort()
        for triplet in result:
            triplet.sort()
        expected.sort()
        for triplet in expected:
            triplet.sort()
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        nums = [-100, 0, 100, 50, -50, 25, -25]
        expected = [[-100, 0, 100], [-50, 0, 50], [-25, 0, 25], [-100, 25, 75], [-100, 50, 50], [-50, 25, 25]]
        result = Solution().threeSum(nums)
        result.sort()
        for triplet in result:
            triplet.sort()
        expected.sort()
        for triplet in expected:
            triplet.sort()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)