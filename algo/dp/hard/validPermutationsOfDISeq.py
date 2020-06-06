class Solution:
    def numPermsDISequence(self, S: str) -> int:
        n = len(S)
        mod = 10**9+7
        dp = [[0]*(n+1) for _ in range(n+1)]

        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(n):
            if S[i] == 'I':
                cur = 0
                for j in range(n-i):
                    cur = (cur + dp[i][j]) % mod
                    dp[i+1][j] = cur
            else:
                cur = 0
                for j in range(n-i-1, -1, -1):
                    cur = (cur + dp[i][j+1]) % mod
                    dp[i+1][j] = cur
        return dp[n][0]


s = Solution()
print(s.numPermsDISequence("DID"))
