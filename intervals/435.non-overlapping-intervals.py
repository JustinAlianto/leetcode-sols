#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start_i
        intervals.sort(key=lambda x: x[0])

        # Get groups of the overlapping intervals
        end_cur = intervals[0][1]
        res = 0

        for start_i, end_i in intervals[1:]:
            if end_cur <= start_i:
                end_cur = end_i
            else:
                res += 1
                end_cur = min(end_cur, end_i)

        return res

        # TIME COMPLEXITY: O(n log n)
        # SPACE COMPLEXITY: O(1)


# @lc code=end
