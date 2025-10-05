#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # +1 because the mid number cannot be the min, since
                # nums[mid] > nums[right]
                left = mid + 1
            else:
                right = mid

        return nums[left]


# @lc code=end
