#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # If all characters are found
            if k == len(word):
                return True

            # Boundary + character check
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            # Mark current cell as visited
            temp = board[i][j]
            board[i][j] = "#"

            # Explore neighbors
            found = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )

            # Restore cell
            board[i][j] = temp

            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False

        # TIME COMPLEXITY: O(m * n * 4^L), where L is length of word
        # SPACE COMPLEXITY: O(L), because recursion depth is proportional to word length


# @lc code=end
