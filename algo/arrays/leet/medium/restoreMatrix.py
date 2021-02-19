from typing import List


class Solution:
    def restoreMatrix(self, rs: List[int], cs: List[int]) -> List[List[int]]:

        n = len(rs)
        m = len(cs)
        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                v = min(rs[i], cs[j])

                res[i][j] += v
                rs[i] -= v
                cs[j] -= v
        return res


rs = [3, 8]
cs = [4, 7]
s = Solution()
print(s.restoreMatrix(rs, cs))
