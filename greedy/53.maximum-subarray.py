#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # IDEA: Keep adding numbers when positive. When we come
        # across a negative number:
        # - Keep track of current sum before the negative
        # - Keep a temporary variable to see if from this negative
        #   value onwards, will the sum remain positive in the end?
        #   - If total sum ever went below 0, restart temporary var = 0
        #   - Else, continue adding
        res = -float("inf")
        tmp = 0

        for num in nums:
            tmp += num

            res = max(res, tmp)

            if tmp < 0:
                tmp = 0

        return res


# @lc code=end
