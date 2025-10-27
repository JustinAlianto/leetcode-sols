#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#


# @lc code=start
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]

        res = ""

        left, right = 0, len(values) - 1

        while left <= right:
            middle = (left + right) // 2

            cur_timestamp = values[middle][1]

            if cur_timestamp <= timestamp:
                res = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
