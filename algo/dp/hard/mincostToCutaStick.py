from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @lru_cache(None)
        def dp(l, r, i, j):

            if i > j:
                return 0

            if i == j:
                return r - l

            cost = float('inf')
            for k in range(i, j+1):
                cost = min(
                    cost, r - l + dp(l, cuts[k], i, k-1) + dp(cuts[k], r, k+1, j))

            return cost

        cuts.sort()
        return dp(0, n, 0, len(cuts)-1)


#n = 7
#cuts = [1, 3, 4, 5]

n = 9
cuts = [5, 6, 1, 4, 2]

s = Solution()
print(s.minCost(n, cuts))
