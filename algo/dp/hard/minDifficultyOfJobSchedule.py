from typing import List
import functools


class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:

        n = len(A)

        @functools.lru_cache(None)
        def dfs(i, d):
            print("i:" + str(i) + " d: " + str(d))
            if d == 1:
                return max(A[i:])

            maxd = 0
            res = float('inf')
            for j in range(i, n - d + 1):
                maxd = max(maxd, A[j])
                res = min(res, maxd + dfs(j+1, d-1))

            return res
        return dfs(0, d)


s = Solution()
print(s.minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], 6))
