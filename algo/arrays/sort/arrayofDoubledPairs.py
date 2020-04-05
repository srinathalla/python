from typing import List
import collections


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        c = collections.Counter(A)
        l = sorted(c, key=abs)
        for x in l:
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        return True


s = Solution()
s.canReorderDoubled([4, -2, 2, -4])
