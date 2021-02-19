from collections import defaultdict
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        self.res = []

        def dfs(g, u, n, path):
            if u == n - 1:
                path.append(u)
                self.res.append(path[::])
                path.remove(u)
                return

            path.append(u)
            for v in g[u]:
                dfs(g, v, n, path)

            path.remove(u)

        g = {}
        n = len(graph)
        for i in range(n):
            g[i] = set()
            for v in graph[i]:
                g[i].add(v)

        dfs(g, 0, n, [])

        return self.res


s = Solution()
graph = [[1, 2], [3], [3], []]

print(s.allPathsSourceTarget(graph))
