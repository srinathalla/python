from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        inc, dec = 1, 1
        res = 1
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                inc = dec + 1
                dec = 1
            elif A[i] < A[i-1]:
                dec = inc + 1
                inc = 1
            else:
                inc = 1
                dec = 1
            res = max(res, inc, dec)
        return res


s = Solution()
print(s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
