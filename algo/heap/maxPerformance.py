import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        # max   (sum S_i) * (min E_i)   , at most K guys
        people = sorted(zip(efficiency, speed), reverse=True)

        ans = 0
        pq = []
        pqsum = 0
        for e, s in people:
            # now considering min effic is e
            heapq.heappush(pq, s)
            pqsum += s
            while len(pq) > k:
                pqsum -= heapq.heappop(pq)
            cand = pqsum * e
            if cand > ans:
                ans = cand

        return ans % MOD


n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 2
s = Solution()
print(s.maxPerformance(n, speed, efficiency, k))
