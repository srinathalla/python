from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(1, len(A)):
            for j in range(i):
                dp[i, A[i] - A[j]] = dp.get((j, A[i] - A[j]), 1) + 1
                print(dp)
        return max(dp.values())


s = Solution()
print(s.longestArithSeqLength([3, 6, 9, 12]))
