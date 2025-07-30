import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        max_length = 0
        n = len(s)
        l = 0
                
        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            max_length = max(max_length, r - l + 1)
        
        return max_length

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = "abcabcbb"
        expected = 3
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)

    def test_example_2(self):
        s = "bbbbb"
        expected = 1
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)

    def test_example_3(self):
        s = "pwwkew"
        expected = 3
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)

    def test_empty_string(self):
        s = ""
        expected = 0
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)

    def test_single_character(self):
        s = "a"
        expected = 1
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)

    def test_long_string_no_repeats(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        expected = 26
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)

    def test_long_string_with_repeats(self):
        s = "dvdf"
        expected = 3
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)

    def test_string_with_spaces(self):
        s = " "
        expected = 1
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)

    def test_string_with_mixed_characters(self):
        s = "au"
        expected = 2
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)