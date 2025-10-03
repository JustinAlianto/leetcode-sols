#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = []

        # Similar idea to Two Sum II to sort the list first
        # *In Python, sorting algorithm use Timsort which uses O(n) space.
        nums.sort()  # O(n log n)

        # O(n)
        for i in range(n):
            # 1st check to prevent duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = 0 - nums[i]

            left = i + 1
            right = n - 1

            # O(n - 1)
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1

                    # 2nd check to prevent duplicate triplets
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        # Time: O(n^2) + O(n log n) ~= O(n^2)
        # Space: O(n)

        return res


# @lc code=end
