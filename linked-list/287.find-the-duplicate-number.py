#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)

        return -1

        # Another method is using Floyd's algorithm, but it's too specific
        # to learn fully
        # slow, fast = 0, 0
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break

        # slow2 = 0
        # while True:
        #     slow = nums[slow]
        #     slow2 = nums[slow2]
        #     if slow == slow2:
        #         return slow


# @lc code=end
