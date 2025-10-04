#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        order = deque()

        mapping = {")": "(", "}": "{", "]": "["}

        for x in s:
            if x in {"(", "{", "["}:
                order.append(x)
            else:
                if not order:
                    return False

                popped = order.pop()

                if mapping[x] != popped:
                    return False

        if order:
            return False

        return True


# @lc code=end
