#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # DP: NUM[i] = NUM[i + 1] + NUM[i + 2]
        # From the big idea, we can tell the optimal flow is backwards

        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]

        return dp[0]

        # TIME COMPLEXITY: O(n)
        # SPACE COMPLEXITY: O(n)

        # Space complexity can be made to O(1) by only storing state i + 1
        # and state i + 2 at any given time

        # # dp represents a temporary variable to store the current iteration
        # # value
        # dp = dp2 = 0
        # dp1 = 1

        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] == "0":
        #         dp = 0
        #     else:
        #         dp = dp1

        #     if i + 1 < len(s) and (s[i] == "1" or
        #        s[i] == "2" and s[i + 1] in "0123456"
        #     ):
        #         dp += dp2

        #     dp, dp1, dp2 = 0, dp, dp1
        # return dp1


# @lc code=end
