from typing import List


class Solution:
    def minDays(self, bd: List[int], m: int, k: int) -> int:

        if len(bd) < m * k:
            return -1

        l = min(bd)
        h = max(bd)
        if l == h:
            return l

        def ready(d):
            count = 0
            b = 0
            for i in range(len(bd)):

                if bd[i] <= d:
                    count += 1
                if count >= k:
                    b += 1
                    count = 0
            return b >= m

        while l < h:
            mid = l + h >> 1

            if ready(mid):
                h = mid
            else:
                l = mid + 1

        return l


bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
s = Solution()
print(s.minDays(bloomDay, m, k))
