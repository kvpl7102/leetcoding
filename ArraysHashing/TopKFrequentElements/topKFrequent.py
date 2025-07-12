import collections
import unittest

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]: # type: ignore
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, numCount in count.items():
            freq[numCount].append(num)

        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

class TestTopKFrequent(unittest.TestCase):
    def test_example_1(self):
        s = Solution()
        nums = [1,1,1,2,2,3]
        k = 2
        # The order does not matter, so we sort both for comparison
        self.assertCountEqual(s.topKFrequent(nums, k), [1,2])

    def test_example_2(self):
        s = Solution()
        nums = [1]
        k = 1
        self.assertCountEqual(s.topKFrequent(nums, k), [1])

    def test_custom_case_1(self):
        s = Solution()
        nums = [4,1,-1,2,-1,2,3]
        k = 2
        self.assertCountEqual(s.topKFrequent(nums, k), [-1,2])

    def test_custom_case_2(self):
        s = Solution()
        nums = [1,2]
        k = 2
        self.assertCountEqual(s.topKFrequent(nums, k), [1,2])

    def test_custom_case_3(self):
        s = Solution()
        nums = [7,7,7,7,8,8,9]
        k = 1
        self.assertCountEqual(s.topKFrequent(nums, k), [7])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)