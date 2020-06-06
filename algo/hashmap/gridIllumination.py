from typing import List
from collections import defaultdict


class Solution:
    def gridIllumination(self, N: int, l: List[List[int]], queries: List[List[int]]) -> List[int]:

        row = [0, 0, 0, -1, -1, -1, 1, 1, 1]
        col = [0, -1, 1, -1, 0, 1, -1, 0, 1]

        r = defaultdict(int)
        c = defaultdict(int)
        dp = defaultdict(int)
        dm = defaultdict(int)
        lamps = defaultdict(bool)

        for ro, co in l:
            r[ro] = r.get(ro, 0) + 1
            c[co] = c.get(co, 0) + 1
            dp[ro + co] = dp.get(ro + co, 0) + 1
            dm[ro - co] = dm.get(ro - co, 0) + 1
            lamps[(ro, co)] = True

        print(r)
        print(c)
        print(dp)
        print(dm)
        res = []
        for ro, co in queries:
            re = r.get(ro, 0) > 0 or c.get(co, 0) > 0 or dp.get(
                ro + co, 0) > 0 or dm.get(ro - co, 0) > 0
            res.append(1 if re is True else 0)

            for i in range(8):
                nr = ro + row[i]
                nc = co + col[i]

                if (nr, nc) in lamps and lamps[(nr, nc)] is True:
                    lamps[(nr, nc)] = False
                    r[nr] -= 1
                    c[nc] -= 1
                    dp[nr + nc] -= 1
                    dm[nr - nc] -= 1
                    lamps[(nr, nc)] = False
        return res


N = 5
lamps = [[0, 0], [1, 0]]
queries = [[1, 1], [1, 1]]


s = Solution()
print(s.gridIllumination(N, lamps, queries))
