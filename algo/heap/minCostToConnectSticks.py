import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        q = []
        for s in sticks:
            heapq.heappush(q, s)

        c = 0
        while len(q) > 1:
            one = heapq.heappop(q)
            two = heapq.heappop(q)
            c += one + two
            heapq.heappush(q, one + two)

        return c


s = Solution()
print(s.connectSticks([1, 8, 3, 5]))
