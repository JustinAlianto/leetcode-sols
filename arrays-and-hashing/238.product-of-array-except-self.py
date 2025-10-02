#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Idea is to multiply forward and then backward

        n = len(nums)
        res = [1 for _ in range(n)]

        cur = 1

        # Multiply forward first
        # Last element should already be fixed at the end of this loop
        for i in range(n):
            res[i] *= cur
            cur *= nums[i]
            # print(res)

        cur = 1

        # Multiply backward
        for i in range(n - 1, -1, -1):
            res[i] *= cur
            cur *= nums[i]
            # print(res)

        return res


# @lc code=end
