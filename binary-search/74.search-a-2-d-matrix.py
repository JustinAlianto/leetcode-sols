#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # IDEA: Find which row the target might be in first,
        #       then find which column in that row the target might be at
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        row = -1

        while top <= bot:
            middle = (top + bot) // 2

            if matrix[middle][0] > target:
                bot = middle - 1
            elif matrix[middle][-1] < target:
                top = middle + 1
            else:
                row = middle
                break

        if row == -1:
            return False

        left, right = 0, COLS - 1

        while left <= right:
            middle = (left + right) // 2

            if matrix[row][middle] > target:
                right = middle - 1
            elif matrix[row][middle] < target:
                left = middle + 1
            else:
                return True

        return False

    # TIME COMPLEXITY: O(log m + log n) ~= O(log mn)
    # SPACE COMPLEXITY: O(1)


# @lc code=end
