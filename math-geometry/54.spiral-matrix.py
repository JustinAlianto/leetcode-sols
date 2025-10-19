#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # IDEA: Have a pointer for each side, keep moving each pointer
        #       in a clockwise manner one-by-one

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])

            # Visually: we are moving the top pointer down by 1
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])

            # Visually: we are moving the right pointer left by 1
            right -= 1

            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])

            # Visually: we are moving the bottom pointer up by 1
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])

            # Visually: we are moving the left pointer right by 1
            left += 1

        return res


# @lc code=end
