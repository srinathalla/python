from typing import List
import bisect
from functools import lru_cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n = len(days)

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0

            a7 = bisect.bisect(days, days[i] + 7)
            if a7 <= n and days[a7 - 1] == days[i] + 7:
                a7 -= 1

            a30 = bisect.bisect(days, days[i] + 30)
            if a30 <= n and days[a30 - 1] == days[i] + 30:
                a30 -= 1

            c2 = costs[0] + dp(i+1)
            c7 = costs[1] + dp(a7)
            c30 = costs[2] + dp(a30)
            cost = min(c2, c7, c30)

            return cost

        return dp(0)


s = Solution()
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(s.mincostTickets(days, costs))
