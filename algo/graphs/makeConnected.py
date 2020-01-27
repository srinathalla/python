from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        graph = [set() for i in range(n)]
        for edge in connections:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        seen = [0 for i in range(n)]
        cc = 0

        for i in range(n):
            if seen[i] == 0:
                cc += 1
                self.dfs(i, graph, seen)

        return cc - 1

    def dfs(self, v, graph, seen):
        if seen[v] == 0:
            seen[v] = 1

            for adjV in graph[v]:
                self.dfs(adjV, graph, seen)


s = Solution()
n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
print(s.makeConnected(n, connections))
