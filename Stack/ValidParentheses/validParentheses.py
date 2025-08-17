import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        
        stack = []

        for c in s:
            if c in parenMap.keys():
                stack.append(c)
            
            else:
                if len(stack) == 0 or stack[-1] in parenMap.values():
                    stack.append(c)
                
                elif parenMap.get(stack[-1]) == c:
                    stack.pop()
                else:
                    stack.append(c)
                
        return True if len(stack) == 0 else False

class TestValidParentheses(unittest.TestCase):

    def test_valid_string_1(self):
        s = "()"
        self.assertTrue(Solution().isValid(s))

    def test_valid_string_2(self):
        s = "()[]{}"
        self.assertTrue(Solution().isValid(s))

    def test_invalid_string_3(self):
        s = "{[]}"
        self.assertTrue(Solution().isValid(s))

    def test_complex_valid_string(self):
        s = "{([])}"
        self.assertTrue(Solution().isValid(s))


if __name__ == '__main__':
    unittest.main()