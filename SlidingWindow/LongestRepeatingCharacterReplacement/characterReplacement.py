import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        result = 0
        left = 0

        for right in range (len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            # max_freq = max(max_freq, count[s[right]])
            
            while (right - left + 1) - max(count.values()) > k: # or put max_freq instead of max(count.values())
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        
        return result

import unittest

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = "ABAB"
        k = 2
        self.assertEqual(Solution().characterReplacement(s, k), 4)

    def test_example_2(self):
        s = "AABABBA"
        k = 1
        self.assertEqual(Solution().characterReplacement(s, k), 4)

    def test_no_replacement_needed(self):
        s = "AAAA"
        k = 0
        self.assertEqual(Solution().characterReplacement(s, k), 4)

    def test_empty_string(self):
        s = ""
        k = 1
        self.assertEqual(Solution().characterReplacement(s, k), 0)

    def test_single_character(self):
        s = "A"
        k = 1
        self.assertEqual(Solution().characterReplacement(s, k), 1)

    def test_all_replacements_possible(self):
        s = "ABBB"
        k = 1
        self.assertEqual(Solution().characterReplacement(s, k), 4)

    def test_complex_case(self):
        s = "ABBCAB"
        k = 2
        self.assertEqual(Solution().characterReplacement(s, k), 5) # ABBCAB -> AAAAAB (k=2, B->A, C->A) or BBBBBB (k=2, A->B, C->B)

if __name__ == '__main__':
    unittest.main()