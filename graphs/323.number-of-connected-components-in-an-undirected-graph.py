# DESCRIPTION:
# There is an undirected graph with n nodes. There is
# also an edges array, where edges[i] = [a, b] means
# that there is an edge between node a and node b in the graph.
# The nodes are numbered from 0 to n - 1.
# Return the total number of connected components in that graph.

# Example 1:
# Input:
# - n = 3
# - edges = [[0,1], [0,2]]
# Output: 1

# Example 2:
# Input:
# - n = 6
# - edges = [[0,1], [1,2], [2,3], [4,5]]
# Output: 2

# Constraints:
# - 1 <= n <= 100
# - 0 <= edges.length <= n * (n - 1) / 2


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        visit = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        res = 0

        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1

        return res
