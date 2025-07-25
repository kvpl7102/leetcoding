import unittest
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        isPalindrome = True

        cleaned = ''.join(c.lower() for c in s if c.isalnum())

        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                isPalindrome = False
            left += 1
            right -= 1

        return isPalindrome

class TestValidPalindrome(unittest.TestCase):
    def test_example_1(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(Solution().isPalindrome(s))

    def test_example_2(self):
        s = "race a car"
        self.assertFalse(Solution().isPalindrome(s))

    def test_example_3(self):
        s = " "
        self.assertTrue(Solution().isPalindrome(s))

    def test_empty_string(self):
        s = ""
        self.assertTrue(Solution().isPalindrome(s))

    def test_single_character(self):
        s = "a"
        self.assertTrue(Solution().isPalindrome(s))

    def test_non_alphanumeric_only(self):
        s = ",."
        self.assertTrue(Solution().isPalindrome(s))

    def test_numbers_and_letters(self):
        s = "0P"
        self.assertFalse(Solution().isPalindrome(s))

    def test_mixed_case(self):
        s = "Madam"
        self.assertTrue(Solution().isPalindrome(s))

if __name__ == '__main__':
    unittest.main()