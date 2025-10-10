#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#


# @lc code=start
import heapq


class MedianFinder:

    def __init__(self):
        # large contains the larger half of all numbers in a min-heap
        self.large = []
        # small contains the smaller half of all numbers in a max-heap
        self.small = []

        # Key: First item from each list will be the middle 2 numbers
        #      among the combined list

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # Use negative numbers to invert Python's min-heap to max-heap
            heapq.heappush(self.small, -num)

        # We want both heaps to be either equal size or differ by 1
        if len(self.large) > len(self.small) + 1:
            popped = heapq.heappop(self.large)
            heapq.heappush(self.small, -popped)
        elif len(self.small) > len(self.large) + 1:
            popped = heapq.heappop(self.small)
            heapq.heappush(self.large, -popped)

        # O(m log n), where m is # of function calls

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -self.small[0]

        return (self.large[0] + (-self.small[0])) / 2

        # O(m)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
