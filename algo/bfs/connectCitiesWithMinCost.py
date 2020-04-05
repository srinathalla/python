from typing import List
import heapq


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:

        g = {i: {} for i in range(1, N + 1)}

        for s, d, c in connections:
            g[s][d] = c
            g[d][s] = c

        q = []
        heapq.heappush(q, (0, 1))
        visited = set()

        sum = 0
        while q:
            c, v = heapq.heappop(q)
            if v in visited:
                continue

            sum += c
            visited.add(v)

            for av in g[v].keys():
                heapq.heappush(q, (g[v][av], av))

        return sum if len(visited) == N else -1


N = 3
connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]

s = Solution()
print(s.minimumCost(N, connections))
