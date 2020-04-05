from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        row = [0, 0, 1]
        col = [1, -1, 0]

        n = len(grid)
        m = len(grid[0])
        visited = set()
        visited.add((0, 0))
        q = []
        q.append((0, 0, 0, 0))

        while q:
            r, c, co, ob = q.pop(0)
            print((r, c, co, ob))
            if r == n - 1 and c == m - 1:
                return co

            for i in range(3):

                ar = r + row[i]
                ac = c + col[i]

                if 0 <= ar < n and 0 <= ac < m and (ar, ac) not in visited and (grid[ar][ac] == 0 or ob + 1 <= k):
                    visited.add((ar, ac))
                    q.append((ar, ac, co + 1, ob + grid[ar][ac]))
        return -1


g = [[0, 0, 0],
     [1, 1, 0],
     [0, 0, 0],
     [0, 1, 1],
     [0, 0, 0]]
k = 1
s = Solution()
print(s.shortestPath(g, k))
