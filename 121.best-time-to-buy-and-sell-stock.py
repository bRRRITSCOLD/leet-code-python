import unittest

# Best Time to Buy and Sell Stock
# Category	Difficulty	Likes	Dislikes
# algorithms	Easy (54.57%)	32316	1236
# Tags
# array | dynamic-programming

# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
# Submissions | Solution

#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for p in prices:
          if p < min_price:
              min_price = p
          elif p - min_price > max_profit:
              max_profit = p - min_price
        return max_profit
        
# @lc code=end




class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        inp = [7,1,5,3,6,4]
        outp = sol.maxProfit(inp)
        self.assertEqual(outp, 5)


        inp = [7,6,4,3,1]
        outp = sol.maxProfit(inp)
        self.assertEqual(outp, 0)

if __name__ == '__main__':
    unittest.main()