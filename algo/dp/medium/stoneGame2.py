from typing import List
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)

        @lru_cache(None)
        def dp(i, M, isA):

            if i == len(piles):
                return (0, 0)

            if i == n - 1:
                return (piles[-1], 0) if isA else (0, piles[-1])

            A = 0
            L = 0
            for x in range(1, min(n+1 - i, 2*M + 1)):
                a1, l1 = dp(i+x, max(M, x), not isA)

                if isA:
                    A = max(A, sum(piles[i:i+x]) + a1)
                    L = l1
                else:
                    L = max(L, sum(piles[i:i+x]) + l1)
                    A = a1

            return (A, L)

        return dp(0, 1, True)[0]


piles = [2, 7, 9, 4, 4]

s = Solution()
print(s.stoneGameII(piles))
