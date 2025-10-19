#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # Get the bit at the i-th spot (from the end/right)
            bit = (n >> i) & 1
            # Put the bit in our result at the i-th spot
            res += bit << (31 - i)

        return res


# @lc code=end
