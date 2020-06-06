from typing import List
from functools import lru_cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])

        @lru_cache(None)
        def dp(r, c1, c2):
            if r == R:
                return 0

            ans = 0
            for a in [-1, 0, 1]:
                nc1 = c1 + a
                if 0 <= nc1 < C:
                    for b in [-1, 0, 1]:
                        nc2 = c2 + b
                        if 0 <= nc2 < C:
                            ans = max(ans, dp(r+1, c1, c2))

            base = grid[r][c1]
            if c1 != c2:
                base += grid[r][c2]

            return ans + base

        return dp(0, 0, C-1)


g = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]

s = Solution()
print(s.cherryPickup(g))
