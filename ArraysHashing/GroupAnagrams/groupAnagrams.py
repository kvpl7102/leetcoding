import collections
import unittest

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Groups anagrams together from a list of strings.

        Args:
            strs: A list of strings.

        Returns:
            A list of lists, where each inner list contains anagrams.
        """

        """
        This is the naive approach of grouping by sorting each string, with time complexity
        of O(n * mlogm) where n is the number of strings, and m is the length of the longest string
        """
        # hashMap = {}
        # for str in strs:
        #     sortedStr = ''.join(sorted(str))
        #     if sortedStr not in hashMap:
        #         hashMap[sortedStr] = [str]
        #     else:
        #         hashMap[sortedStr].append(str)
        # return list(hashMap.values())

        """
        This is the approach by using the character count array for each string, then grouping the anagram by it, 
        with the complexity of O(n * m)
        """
        hashMap = collections.defaultdict(list)
        for str in strs:
            charCount = [0] * 26 # frequency array of alphabet characters
            for char in str:
                charCount[ord(char) - ord('a')] += 1
            
            hashMap[tuple(charCount)].append(str)
                
        return list(hashMap.values())

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertAnagramsEqual(self, list1, list2):
        """
        Custom assertion to compare lists of anagram groups.
        Sorts each inner list and the outer list for a stable comparison.
        """
        sorted_list1 = sorted([sorted(sublist) for sublist in list1])
        sorted_list2 = sorted([sorted(sublist) for sublist in list2])
        self.assertEqual(sorted_list1, sorted_list2)

    def test_example_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        result = self.solution.groupAnagrams(strs)
        self.assertAnagramsEqual(result, expected)

    def test_empty_string(self):
        strs = [""]
        expected = [[""]]
        result = self.solution.groupAnagrams(strs)
        self.assertAnagramsEqual(result, expected)

    def test_single_character_strings(self):
        strs = ["a", "b", "c", "a"]
        expected = [["a", "a"], ["b"], ["c"]]
        result = self.solution.groupAnagrams(strs)
        self.assertAnagramsEqual(result, expected)

    def test_no_strings(self):
        strs = []
        expected = []
        result = self.solution.groupAnagrams(strs)
        self.assertAnagramsEqual(result, expected)

    def test_all_anagrams(self):
        strs = ["abc", "bca", "cab"]
        expected = [["abc", "bca", "cab"]]
        result = self.solution.groupAnagrams(strs)
        self.assertAnagramsEqual(result, expected)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)