class Solution:
    def countVowelPermutation(self, n: int) -> int:

        dp = [[0]*5 for _ in range(n+1)]
        m = 1000000007

        for i in range(5):
            dp[1][i] = 1

        for i in range(2, n+1):
            dp[i][0] += (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % m
            dp[i][1] += (dp[i-1][0] + dp[i-1][2]) % m
            dp[i][2] += (dp[i-1][1] + dp[i-1][3]) % m
            dp[i][3] += (dp[i-1][2]) % m
            dp[i][4] += (dp[i-1][2] + dp[i-1][3]) % m

        res = 0
        for no in dp[n]:
            res = (res + no) % m
        return res


s = Solution()
print(s.countVowelPermutation(1))
print(s.countVowelPermutation(2))
print(s.countVowelPermutation(5))
