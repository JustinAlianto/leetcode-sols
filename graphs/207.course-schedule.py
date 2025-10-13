#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}

        for c, pre in prerequisites:
            courses[c].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if courses[course] == []:
                return True

            visited.add(course)

            for pre in courses[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)
            courses[course] = []

            return True

        for c in courses:
            if not dfs(c):
                return False

        return True

        # In a typical graph adjacency list for traversal only,
        # list is the canonical structure — because:
        # - The number of neighbors is small on average.
        # - You rarely need O(1) membership checks.
        # - The order and memory layout help recursion performance.

        # Even though lookup (x in set) is O(1), iteration has higher
        # constant overhead due to hash computations and pointer dereferencing.


# @lc code=end
