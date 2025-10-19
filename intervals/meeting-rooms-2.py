# DESCRIPTION:
# Given an array of meeting time interval objects consisting
# of start and end times [[start_1,end_1],[start_2,end_2],...]
# (start_i < end_i), find the minimum number of days required
# to schedule all meetings without any conflicts.

# Note: (0,8),(8,10) is not considered a conflict at 8.

# Example 1:
# Input: intervals = [(0,40),(5,10),(15,20)]
# Output: 2
# Explanation:
# day1: (0,40)
# day2: (5,10),(15,20)

# Example 2:
# Input: intervals = [(4,9)]
# Output: 1

# Constraints:
# - 0 <= intervals.length <= 500
# - 0 <= intervals[i].start < intervals[i].end <= 1,000,000


import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        min_heap = []

        for interval in intervals:
            # Check the case when an interval has no overlap and pop it
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)
