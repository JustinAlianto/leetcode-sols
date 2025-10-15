#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#


# @lc code=start
class Solution:
    def helper(self, curr_nums):
        rob1, rob2 = 0, 0

        for n in curr_nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    def rob(self, nums: List[int]) -> int:
        # DP: f(n) = max(f(0 : n - 1), f(1 : n))

        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


# @lc code=end
