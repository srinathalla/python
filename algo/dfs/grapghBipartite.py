from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        colors = [0]*n

        def dfs(v, c):
            if colors[v] != 0:
                return colors[v] == c

            colors[v] = c
            for av in graph[v]:
                if dfs(av, -c) == False:
                    return False

            return True

        for i in range(n):
            if colors[i] == 0 and dfs(i, 1) == False:
                return False

        return True


g = [[1, 3], [0, 2], [1, 3], [0, 2]]
s = Solution()
print(s.isBipartite(g))
