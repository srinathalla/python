import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        pq = []

        for a in nums:
            heapq.heappush(pq, a)

            if len(pq) > k:
                heapq.heappop(pq)

        return heapq.heappop(pq)


arr = [3, 2, 1, 5, 6, 4]
k = 2
s = Solution()
print(s.findKthLargest(arr, k))
