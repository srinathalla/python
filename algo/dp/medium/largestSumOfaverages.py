from typing import List
from functools import lru_cache


class Solution:
    def largestSumOfAverages(self, A: List[int], k: int) -> float:

        n = len(A)

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0

            ans = 0
            s = 0
            for j in range(i, min(n, i+k)):
                s += A[j]
                ans = max(ans, s//(j-i+1) + dp(j+1))

            return ans

        return dp(0)


A = [9, 1, 2, 3, 9]
s = Solution()
print(s.largestSumOfAverages(A, 3))
