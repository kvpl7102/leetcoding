import unittest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
        
class TestIsAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_anagram(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))

    def test_not_anagram(self):
        self.assertFalse(self.solution.isAnagram("rat", "car"))

    def test_different_lengths(self):
        self.assertFalse(self.solution.isAnagram("a", "ab"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isAnagram("", ""))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)