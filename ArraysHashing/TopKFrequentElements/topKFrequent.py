import collections
import heapq
import unittest

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Approach 1: Using collections.Counter and sorting (simpler for Python)
        # frequency_map = collections.Counter(nums)
        # sorted_items = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)
        # result = [item[0] for item in sorted_items[:k]]
        # return result

        # Approach 2: Using a min-heap (more generalizable to other languages)
        # frequency_map = collections.Counter(nums)
        # min_heap = [] # Stores (frequency, number)

        # for num, freq in frequency_map.items():
        #     heapq.heappush(min_heap, (freq, num))
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        
        # result = [item[1] for item in min_heap]
        # return result

        

        return []

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