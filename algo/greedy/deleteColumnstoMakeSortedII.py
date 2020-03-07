from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res, n, m = 0, len(A), len(A[0])
        unsorted = set(range(n-1))
        for i in range(m):
            if any(A[j][i] > A[j+1][i] for j in unsorted):
                res += 1
            else:
                unsorted -= {j for j in unsorted if A[j][i] < A[j+1][i]}
        return res


A = ["xga", "xfb", "yfa"]
s = Solution()
print(s.minDeletionSize(A))
