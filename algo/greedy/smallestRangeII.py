from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], k: int) -> int:

        n = len(A)
        mid = (n + 1)//2 if n % 2 == 1 else n//2
        A.sort()

        B = [A[i] + k for i in range(mid)]
        C = [A[i] - k for i in range(mid, len(A))]

        D = B + C

        return max(D) - min(D)


s = Solution()
A = [7, 8, 8]

K = 5
print(s.smallestRangeII(A, K))
