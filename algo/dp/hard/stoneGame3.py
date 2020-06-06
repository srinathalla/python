from typing import List


class Solution:
    def stoneGameIII(self, A: List[int]) -> str:
        N = len(A)
        dp = [float('-inf')] * (N + 1)
        WA = "Alice"
        WB = "Bob"
        WT = "Tie"
        dp[-1] = 0

        for i in range(N-1, -1, -1):
            for j in range(3):
                if i + j >= N:
                    continue
                dp[i] = max(dp[i], sum([A[i+k]
                                        for k in range(j+1)]) - dp[i+j+1])

        if dp[0] > 0:
            return WA
        elif dp[0] < 0:
            return WB
        return WT


s = Solution()
print(s.stoneGameIII([1, 2, 3, 7]))
