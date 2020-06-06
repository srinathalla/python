from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)
        r = sum(weights)

        def canShip(wt):
            need = 1
            curr = 0
            for w in weights:
                if curr + w > wt:
                    curr = 0
                    need += 1
                curr += w
            return need <= D

        while l <= r:
            m = (l + r) >> 1

            print(l)
            print(r)
            if canShip(m):
                r = m - 1
            else:
                l = m + 1

        return l


s = Solution()
print(s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
