import unittest

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]

            max_profit = max(max_profit, prices[i] - min_price)
            
        return max_profit

class TestMaxProfit(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().maxProfit([7,1,5,3,6,4]), 5)

    def test_example_two(self):
        self.assertEqual(Solution().maxProfit([7,6,4,3,1]), 0)

    def test_empty_prices(self):
        self.assertEqual(Solution().maxProfit([]), 0)

    def test_single_price(self):
        self.assertEqual(Solution().maxProfit([1]), 0)

    def test_two_prices_profit(self):
        self.assertEqual(Solution().maxProfit([1, 2]), 1)

    def test_two_prices_no_profit(self):
        self.assertEqual(Solution().maxProfit([2, 1]), 0)

    def test_prices_with_negative_profit_potential(self):
        self.assertEqual(Solution().maxProfit([3,2,6,5,0,3]), 4)

    def test_prices_with_peak_at_end(self):
        self.assertEqual(Solution().maxProfit([2,4,1]), 2)

if __name__ == '__main__':
    unittest.main()