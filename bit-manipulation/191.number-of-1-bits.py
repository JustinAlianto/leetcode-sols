#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#


# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            res += 1 if n & 1 else 0  # OR res += n % 2
            # Shift bits to the right by 1
            n >>= 1

            # ANOTHER METHOD
            # n &= n - 1  # This skips all the 0s in within a number
            # res += 1
        return res

        # TIME COMPLEXITY: O(32) ~= O(1)


# @lc code=end
