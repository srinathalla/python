import collections
import heapq
from typing import List
from collections import Counter


class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:

        mod = 10**9 + 7
        hc.sort()
        vc.sort()
        n = len(hc)
        m = len(vc)

        vp = 0
        mv = 0
        for j in range(m):
            ma = max(mv, (vc[j] - vp))
            vp = vc[j]
        mv = max(mv, w - vp)

        hp = 0
        mh = 0
        for i in range(n):
            mh = max(ma, (hc[i] - hp))
            hp = hc[i]
        mh = max(mh, (h - hp))

        return (mv * mh) % mod


h = 5
w = 4
hc = [3, 1]
vc = [1]


s = Solution()

print(s.maxArea(h, w, hc, vc))
