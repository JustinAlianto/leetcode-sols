#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#


# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # Stores (tmp, idx)

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1][1] - i

            stack.append((temperatures[i], i))

        return res

    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(n)


# @lc code=end
