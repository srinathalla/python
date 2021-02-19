from functools import lru_cache
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:

        n = len(A)
        ps = [0] * (n + 1)

        for i in range(n):
            ps[i+1] = ps[i] + A[i]

        res = 0
        INFI = float('-inf')

        @lru_cache(None)
        def ms(i, j, k):
            if i > j:
                return INFI

            if j - i + 1 == k:
                return ps[j+1] - ps[i]

            if j - i + 1 < k:
                return INFI

            res = 0
            for p in range(i, j-k+2):
                res = max(res, ps[p+k] - ps[p] + ms(p+1, j, k))

            return res

        return ms(0, n-1, L)


A = [0, 6, 5, 2, 2, 5, 1, 9, 4]
L = 1
M = 2
s = Solution()
print(s.maxSumTwoNoOverlap(A, L, M))
