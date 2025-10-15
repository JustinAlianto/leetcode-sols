#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # IDEA: Bottom-Up DP
        # - At each value (0 to amount), we find the fewest number of
        #   needed to get that value, iterating through all coins each time.

        # amount + 1 is the maximum, but this can be inf too
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for val in range(1, amount + 1):
            for coin in coins:
                if val - coin >= 0:
                    dp[val] = min(dp[val], 1 + dp[val - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1


# @lc code=end
