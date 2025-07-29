class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
                
        return max_area
# Test Cases
test_cases = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  
    ([1, 1], 1),                     
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 1], 2),
    ([2, 3, 4, 5, 18, 17, 6], 17),
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25), 
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 25) 
]

# Run tests
if __name__ == "__main__":
    sol = Solution()
    for i, (height_array, expected_output) in enumerate(test_cases):
        result = sol.maxArea(height_array)
        print(f"Test Case {i+1}:")
        print(f"  Input: {height_array}")
        print(f"  Expected: {expected_output}")
        print(f"  Got: {result}")
        assert result == expected_output, f"Test Case {i+1} Failed: Expected {expected_output}, Got {result}"
        print("  Status: Passed\n")