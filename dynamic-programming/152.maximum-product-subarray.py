#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        # curMin is to allow situations with negative values and to
        # keep track the largest absolute value even if it's negative.
        # This is so that if we have a negative value down the line, we
        # multiply it to be positive and potentially, be the max product.
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)

        return res


# @lc code=end
