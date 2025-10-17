#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Visualize with a grid for the 2 strings.
        # Use a bottom-up approach and initialize 0s for out of bound "invisible" strings

        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # Iterate from bottom-right back to top-left
        # - Note that if the value in text1 matches the value in text2,
        #   we are traversing diagonally immediately
        # - Otherwise, we are checking between the left or top value
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # Here, we check the max of the bottom value or the right value
                    # because the characters don't match
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]


# @lc code=end
