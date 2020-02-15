from typing import List
from itertools import *


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        values = []
        for i in range(n):
            for j in range(m):
                values.append(grid[i][j])

        arrIter = iter(values[-k:] + values[:-k])

        return [[next(arrIter) for _ in range(m)] for _ in range(n)]


s = Solution()
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
grid = s.shiftGrid(grid, k)
print(grid)
