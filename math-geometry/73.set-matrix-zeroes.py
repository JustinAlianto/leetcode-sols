#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#


# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # IDEA:
        # - Get all rows and columns that need to be zero-ed
        # - Run through the matrix and zero all the needed rows & columns

        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = [False] * ROWS, [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        for r in range(ROWS):
            for c in range(COLS):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0

        # TIME COMPLEXITY: O(mn)
        # SPACE COMPLEXITY: O(m + n)


# @lc code=end
