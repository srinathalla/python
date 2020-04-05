from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        q = []
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))

        if len(q) == 0:
            return -1

        row = [0, 0, -1, 1]
        col = [-1, 1, 0, 0]
        dist = 1
        while q:

            size = len(q)
            for i in range(size):
                r, c = q.pop(0)

                for j in range(4):
                    ar = r + row[j]
                    ac = c + col[j]

                    if 0 <= ar < n and 0 <= ac < m and grid[ar][ac] == 0:
                        grid[ar][ac] = grid[r][c] + 1
                        q.append((ar, ac))
                        dist = max(dist, grid[ar][ac])
        return dist - 1 if dist > 1 else -1


s = Solution()
g = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
print(s.maxDistance(g))
