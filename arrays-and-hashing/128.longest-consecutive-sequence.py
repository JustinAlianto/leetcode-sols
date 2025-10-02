#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Treat each number as the beginning of a sequence,
        # hence, the check 'num - 1 not in nums'

        nums = set(nums)

        longest_count = 0

        # The below initialization is true and correct, but it doesn't handle an empty list
        # longest_count = 1  # Each number is a sequence of 1 at least

        for num in nums:
            if num - 1 not in nums:
                cur = num + 1
                while cur in nums:
                    cur += 1

                longest_count = max(longest_count, cur - num)

        return longest_count


# @lc code=end
