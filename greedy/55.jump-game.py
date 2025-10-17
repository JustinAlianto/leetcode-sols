#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1

        min_idx = n

        for i in range(n - 1, -1, -1):
            if nums[i] + i >= min_idx:
                min_idx = i

        return min_idx == 0


# @lc code=end
