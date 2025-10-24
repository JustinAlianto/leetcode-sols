#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Iterate rows
        for row in range(9):
            seen = set()

            # Iterate columns
            for i in range(9):
                cell = board[row][i]

                if cell == ".":
                    continue
                elif cell in seen:
                    return False
                else:
                    seen.add(cell)

        # Iterate columns
        for col in range(9):
            seen = set()

            # Iterate rows
            for i in range(9):
                cell = board[i][col]

                if cell == ".":
                    continue
                elif cell in seen:
                    return False
                else:
                    seen.add(cell)

        # Iterate sub-boxes
        for box in range(9):
            seen = set()

            row_offset, col_offset = box // 3, box % 3
            # Iterate rows
            for i in range(3):
                # Iterate columns
                for j in range(3):
                    cell = board[i + row_offset * 3][j + col_offset * 3]

                    if cell == ".":
                        continue
                    elif cell in seen:
                        return False
                    else:
                        seen.add(cell)

        return True


# @lc code=end
