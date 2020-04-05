from typing import List
import heapq


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:

        g = {i: {} for i in range(1, N + 1)}

        for s, d, c in connections:
            g[s][d] = c
            g[d][s] = c

        q = []
        heapq.heappush(q, (0, 0, 1))
        visited = set()

        s = 0
        while q:
            c, pc, v = heapq.heappop(q)
            if v in visited:
                continue

            s += (c + pc)
            visited.add(v)

            for av in g[v].keys():
                heapq.heappush(q, (c + g[v][av], -c, av))

        return s if len(visited) == N else -1


s = Solution()
print(s.minimumCost(3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]))
