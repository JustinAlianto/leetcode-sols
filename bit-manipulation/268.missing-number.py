#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#


# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        # (1 + 2 + ... + n) - sum(nums) will give the missing number
        for i in range(len(nums)):
            res += i - nums[i]

        return res

        # XOR METHOD:
        # n = len(nums)
        # xorr = n

        # XOR doesn't care about ordering, so:
        # [0, 1, ..., n] ^ nums will eventually give the missing number
        # for i in range(n):
        #     xorr ^= i ^ nums[i]

        # return xorr


# @lc code=end
