#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m -> row, n -> col

        # IDEA: Work backwards from the finish, because the base case
        #       is when you are at the finish

        # NOTE: The most bottom row will always only have 1 way
        #       of getting to the finish, since you can't go down anymore
        #       and you can only keep going right till the finish
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                # That row[j] represents the row below this current newRow
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]

    # TIME COMPLEXITY: O(mn)
    # SPACE COMPLEXITY: O(n)


# @lc code=end
