# DESCRIPTION:
# Given n nodes labeled from 0 to n - 1 and a list of undirected
# edges (each edge is a pair of nodes), write a function to check
# whether these edges make up a valid tree. A valid tree is CONNECTED
# and has NO CYCLES.

# Example 1:
# Input:
# - n = 5
# - edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true

# Example 2:
# Input:
# - n = 5
# - edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false

# Note:
# You can assume that no duplicate edges will appear in edges.
# Since all edges are undirected, [0, 1] is the same as [1, 0]
# and thus will not appear together in edges.


# Constraints:
# - 1 <= n <= 100
# - 0 <= edges.length <= n * (n - 1) / 2


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node, prev):
            # Cycle Check
            if node in visit:
                return False

            visit.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n

    # TIME/SPACE COMPLEXITY: O(V + E)
