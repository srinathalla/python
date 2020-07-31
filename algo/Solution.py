from typing import List


class Solution:
    def numSubseq(self, arr: List[int], k: int) -> int:
        n = len(arr)
        mod = 10**9 + 7
        dp = [[0 for j in range(n + 1)]
              for i in range(k + 1)]
        for i in range(1, k + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                if arr[j - 1] <= i and arr[j - 1] > 0:
                    dp[i][j] = (dp[i][j] + dp[i - arr[j - 1]][j - 1] + 1) % mod
        return dp[k][n]


s = Solution()
print(s.numSubseq([3, 5, 6, 7], 9))
