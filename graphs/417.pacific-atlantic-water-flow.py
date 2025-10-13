#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#


# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # IDEA: Get the cells that can have water flow to either ocean through
        #       the bordering cells. Find the intersection of the 2 sets of cells.
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        pac, atl = set(), set()

        m, n = len(heights), len(heights[0])

        res = []

        def dfs(col_i, row_i, ocean_set, prev_height):
            # Check:
            # - Valid bounds
            # - Not yet in visited set
            # - Height >= prev_height
            if (
                0 <= col_i < n
                and 0 <= row_i < m
                and prev_height <= heights[row_i][col_i]
                and (row_i, col_i) not in ocean_set
            ):
                ocean_set.add((row_i, col_i))

                for x, y in directions:
                    dfs(col_i + x, row_i + y, ocean_set, heights[row_i][col_i])

            return

        for col in range(n):
            # Check top cells that flow to Pacific Ocean
            dfs(col, 0, pac, heights[0][col])
            # Check bottom cells that flow to Atlantic Ocean
            dfs(col, m - 1, atl, heights[m - 1][col])

        for row in range(m):
            # Check left cells that flow to Pacific Ocean
            dfs(0, row, pac, heights[row][0])
            # Check right cells that flow to Atlantic Ocean
            dfs(n - 1, row, atl, heights[row][n - 1])

        for cell in pac.intersection(atl):
            res.append([cell[0], cell[1]])

        return res


# @lc code=end
