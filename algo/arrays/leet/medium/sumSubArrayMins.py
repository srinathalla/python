from typing import List
import collections


class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        c = 0
        m = collections.defaultdict(int)
        m[0] = 1
        res = 0

        for a in arr:
            c ^= a
            if c in m:
                res += m[c]

            m[c] += 1

        print(m)
        return res


A = [1, 3, 5, 7, 9]

s = Solution()
print(s.countTriplets(A))
