#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#


# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # IDEA:
        # - Use XOR to handle bit 0 + bit 0/1 cases (a ^ b)
        # - Use AND to handle when there is a carry over with
        #   bit 1 + bit 1. Need to shift to the left though (a & b << 1)
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)


# @lc code=end
