from collections import defaultdict


from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        ans = INF = float('inf')

        for v, w in edges:
            for u in g[v] & g[w]:
                deg = len(g[u]) + len(g[v]) + len(g[w])
                deg -= 6
                if deg < ans:
                    ans = deg
        return ans if ans < INF else -1


n = 6
edges = [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]
sol = Solution()
print(sol.minTrioDegree(n, edges))
