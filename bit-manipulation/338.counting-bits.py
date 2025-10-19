#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#


# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            # This keeps updating the highest number that
            # is a 2^n and <= i
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        # METHOD 2:
        # for i in range(n + 1):
        #     dp[i] = dp[i >> 1] + (i & 1)

        return dp


# @lc code=end
