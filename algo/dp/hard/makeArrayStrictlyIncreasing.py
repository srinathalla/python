import collections
import bisect
from typing import List
from functools import lru_cache


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:

        n = len(cost)
        dp = [[False]*(target + 1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, target+1):
                if j >= cost[i-1]:
                    dp[i][j] = dp[i][j - cost[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        return "0" if dp[n][target] is False else


#cost = [2, 4, 2, 5, 3, 2, 5, 5, 4]
#target = 739

cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
target = 9

s = Solution()
print(s.largestNumber(cost, target))
