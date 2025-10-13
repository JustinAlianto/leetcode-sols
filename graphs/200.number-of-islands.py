#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        num_islands = 0

        # (i, j) is an unvisited land
        def dfs(i, j):
            for d_i, d_j in directions:
                new_i, new_j = i + d_i, j + d_j

                # Check in-bound and unvisited "1" land
                if m > new_i >= 0 and n > new_j >= 0 and grid[new_i][new_j] == "1":
                    grid[new_i][new_j] = "0"
                    dfs(new_i, new_j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j):
                    grid[i][j] = "0"
                    dfs(i, j)
                    num_islands += 1

        return num_islands

    # SKIP using visited set by replacing a visited node with "0"


# @lc code=end
