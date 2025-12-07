from typing import List
import unittest

class Solution:
    def Bai2(self, s: str) -> int:
        hashSet = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            longest = max(longest, r - l + 1)

        return longest

class TestBai2(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution().Bai2("abcabcbb"), 3)
    
    def test_2(self):
        self.assertEqual(Solution().Bai2("bbbbb"), 1)
    
    def test_3(self):
        self.assertEqual(Solution().Bai2("pwwkew"), 3)

    def test_4(self):
        self.assertEqual(Solution().Bai2("abcdafc"), 5)

if __name__ == '__main__':
    unittest.main()   
