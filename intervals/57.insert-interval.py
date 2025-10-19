#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#


# @lc code=start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        start_new, end_new = newInterval[0], newInterval[1]

        for i in range(len(intervals)):
            start_i, end_i = intervals[i][0], intervals[i][1]

            # CASE 1: If newInterval OR the updated new interval ends before the start
            #         of an interval
            if end_new < start_i:
                res.append([start_new, end_new])

                return res + intervals[i:]
            # CASE 2: Purely when an interval is before the start of newInterval
            elif end_i < start_new:
                res.append([start_i, end_i])
            # CASE 3: When newInterval has any overlap, keep updating the boundaries
            else:
                start_new, end_new = min(start_new, start_i), max(end_new, end_i)

        res.append([start_new, end_new])

        return res

        # if not intervals:
        #     return [newInterval]

        # res = []

        # new_start, new_end = newInterval[0], newInterval[1]

        # prev_start, prev_end = float("inf"), 0

        # merging, merged = False, False

        # for start, end in intervals:
        #     if end < new_start or start > new_end:
        #         if prev_end < new_start and new_end < end:
        #             res.append(newInterval)
        #             merged = True

        #         if merging:
        #             res.append([prev_start, prev_end])
        #             merging = False
        #             merged = True

        #         res.append([start, end])
        #         prev_end = end
        #         continue

        #     merging = True
        #     prev_start, prev_end = min(prev_start, start, new_start), max(
        #         prev_end, end, new_end
        #     )

        # if not res:
        #     return [[prev_start, prev_end]]

        # if not merged:
        #     if new_end < res[0][0]:
        #         res = [newInterval] + res
        #     elif prev_start != float("inf") and prev_end >= new_end:
        #         res.append([prev_start, prev_end])
        #     else:
        #         res.append(newInterval)

        # return res


# @lc code=end
