#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need_map = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in need_map:
                return [need_map[need], i]

            need_map[nums[i]] = i

        # Space: O(n)

        return []


# @lc code=end
