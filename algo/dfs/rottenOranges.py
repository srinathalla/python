from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        m3 = set()
        res = 0

        def dfs(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:

                grid[i][j] = -1
                if (i < n - 1 and grid[i+1][j] == 2) or (i > 0 and grid[i-1][j] == 2) or (j > 0 and grid[i][j-1] == 2) or (j < m-1 and grid[i][j+1]) == 2:
                    grid[i][j] == 3
                    m3.add((i, j))

                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j-1)
                dfs(i, j+1)

                grid[i][j] = 1

        while True:
            m3.clear()
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        dfs(i, j)

            if len(m3) == 0:
                break

            for i, j in m3:
                grid[i][j] = 2

            res += 1

        if any(v == 1 for v in row for row in grid):
            return -1
            
        return res


g = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
s = Solution()
print(s.orangesRotting(g))
