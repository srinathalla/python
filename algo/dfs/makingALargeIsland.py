from typing import List
from collections import defaultdict


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        map = defaultdict(int)
        map[0] = 0

        n = len(grid)
        m = len(grid[0])

        def paint(i, j, color):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:

                grid[i][j] = color
                return 1 + paint(i+1, j, color) + paint(i-1, j, color) + paint(i, j+1, color) + paint(i, j-1, color)
            else:
                return 0

        color = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    map[color] = paint(i, j, color)
                    color += 1

        res = map.get(2, 0)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    cells = set()
                    cells.add(grid[i+1][j] if i < n - 1 else 0)
                    cells.add(grid[i-1][j] if i > 0 else 0)
                    cells.add(grid[i][j + 1] if j < m - 1 else 0)
                    cells.add(grid[i][j - 1] if j > 0 else 0)

                    val = 1
                    for c in cells:
                        val += map[c]
                    res = max(res, val)
        return res


s = Solution()
print(s.largestIsland([[1, 1], [1, 1]]))
