#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right

            # left to mid is increasing only
            if nums[mid] > nums[left]:
                if target > nums[left] and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            # mid to right is increasing only
            else:
                if target > nums[mid] and target < nums[right]:
                    left = mid + 1
                else:
                    right = mid

        return left if nums[left] == target else -1


# @lc code=end
