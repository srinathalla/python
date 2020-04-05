from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, k: int) -> int:

        g = {i: [] for i in range(1, N+1)}

        for time in times:
            g[time[0]].append((time[1], time[2]))

        visited = set()

        ans = 0
        q = []
        heapq.heappush(q, (0, k))

        while q:
            time = heapq.heappop(q)
            v = time[1]
            c = time[0]
            if v in visited:
                continue

            visited.add(v)
            ans = c

            for av in g[v]:
                heapq.heappush(q, (c + av[1], av[0]))

        return ans if len(visited) == N else -1


times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
N = 3
K = 1
s = Solution()
print(s.networkDelayTime(times, N, K))
