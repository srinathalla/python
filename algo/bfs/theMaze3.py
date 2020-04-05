import heapq
from typing import List


class Solution:
    def findShortestWay(self, A: List[List[int]], ball: List[int], hole: List[int]) -> str:
        ball, hole = tuple(ball), tuple(hole)
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for dr, dc, di in [(-1, 0, 'u'), (0, 1, 'r'),
                               (0, -1, 'l'), (1, 0, 'd')]:
                cr, cc, dist = r, c, 0
                while (0 <= cr + dr < R and
                        0 <= cc + dc < C and
                        not A[cr+dr][cc+dc]):
                    cr += dr
                    cc += dc
                    dist += 1
                    if (cr, cc) == hole:
                        break
                yield (cr, cc), di, dist

        pq = [(0, '', ball)]
        seen = set()
        while pq:
            dist, path, node = heapq.heappop(pq)
            if node in seen:
                continue
            if node == hole:
                return path
            seen.add(node)
            for nei, di, nei_dist in neighbors(*node):
                heapq.heappush(pq, (dist+nei_dist, path+di, nei))

        return "impossible"


g = [[0, 0, 0, 0, 0],
     [1, 1, 0, 0, 1],
     [0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1],
     [0, 1, 0, 0, 0]]

s = Solution()
print(s.findShortestWay(g, [4, 3], [0, 1]))
