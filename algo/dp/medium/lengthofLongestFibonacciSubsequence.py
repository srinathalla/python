from typing import List


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        s = set(A)
        res = 2
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                a, b, l = A[i], A[j], 2
                while a+b in s:
                    a, b, l = b, a+b, l+1

                res = max(res, l)
        return res


s = Solution()
print(s.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
