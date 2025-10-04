#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1

        profit = 0

        while right < len(prices):
            cur_profit = prices[right] - prices[left]

            # Logic: We want our buy (left) to always be at the minimum
            # - Whenever we are at a loss, no point continuing with that
            # buying price. Move left
            if prices[right] < prices[left]:
                left = right

            right += 1
            profit = max(profit, cur_profit)

        return profit


# @lc code=end
