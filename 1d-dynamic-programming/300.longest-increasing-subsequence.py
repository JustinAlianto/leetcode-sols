#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    # Keep in mind, we still have to compare res[i]
                    # because there can be multiple subsequences being
                    # checked for each i
                    res[i] = max(res[i], 1 + res[j])

        return max(res)


# @lc code=end
