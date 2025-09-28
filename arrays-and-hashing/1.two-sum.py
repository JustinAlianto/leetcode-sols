#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_map = {}

        for i, num in enumerate(nums):
            if num not in val_map:
                val_map[target - num] = i
            else:
                return [val_map[num], i]


# @lc code=end
