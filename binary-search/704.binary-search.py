#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1

        # BELOW APPROACH IS NOT SPACE OPTIMAL (O(log n) due to the recursions)
        # if not nums:
        #     return -1

        # n = len(nums)

        # middle = n // 2

        # if nums[middle] == target:
        #     return middle
        # elif nums[middle] > target:
        #     return self.search(nums[:middle], target)
        # else:
        #     res = self.search(nums[middle + 1 :], target)
        #     return res if res == -1 else middle + 1 + res


# @lc code=end
