#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest_pile = max(piles)

        left, right = 1, largest_pile

        k = largest_pile

        while left <= right:
            tmp_k = (left + right) // 2

            cur_h = 0

            for p in piles:
                cur_h += math.ceil(p / tmp_k)

            if cur_h <= h:
                k = tmp_k
                right = tmp_k - 1
            else:
                left = tmp_k + 1

        return k


# @lc code=end
