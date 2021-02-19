from functools import lru_cache
from typing import List


class Solution:
    def stoneGameV(self, sv: List[int]) -> int:

        n = len(sv)
        ps = [0] * (n+1)

        for i in range(n):
            ps[i+1] = ps[i] + sv[i]

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0

            cost = 0
            for k in range(i, j):
                if ps[k+1] - ps[i] > ps[j+1] - ps[k+1]:
                    cost = max(cost, ps[j+1] - ps[k+1] + dp(k+1, j))
                elif ps[k+1] - ps[i] < ps[j+1] - ps[k+1]:
                    cost = max(cost, ps[k+1] - ps[i] + dp(i, k))
                else:
                    cost = max(cost, max(dp(i, k), dp(k+1, j)))
            return cost

        return dp(0, n-1)


sv = [6, 2, 3, 4, 5, 5]
s = Solution()
print(s.stoneGameV(sv))
