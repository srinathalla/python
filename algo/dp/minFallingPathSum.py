from typing import List


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                best = A[i - 1][j]
                if j + 1 < len(A):
                    best = min(best, A[i - 1][j + 1])
                if j > 0:
                    best = min(best, A[i - 1][j - 1])

                A[i][j] += best

        minVal = float('inf')
        for no in A[len(A) - 1]:
            minVal = min(minVal, no)

        return minVal


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.minFallingPathSum(A))
