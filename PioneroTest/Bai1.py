from typing import List

class Solution:
    def Bai1(self, nums: List[int]) -> int: 
        hashSet = set()

        for i in range(len(nums)):
            if nums[i] in hashSet:
                hashSet.remove(nums[1])
            hashSet.add(nums[i])

        return 1
    