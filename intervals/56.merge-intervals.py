#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key=lambda x: x[0])

        start_cur, end_cur = intervals[0]

        for start_i, end_i in intervals[1:]:
            if end_cur < start_i:
                res.append([start_cur, end_cur])
                start_cur, end_cur = start_i, end_i
            elif end_i < start_cur:
                res.append([start_i, end_i])
            else:
                start_cur, end_cur = min(start_cur, start_i), max(end_cur, end_i)

        res.append([start_cur, end_cur])

        return res

        # TIME COMPLEXITY: O(n log n)
        # SPACE COMPLEXITY: O(n)


# @lc code=end
