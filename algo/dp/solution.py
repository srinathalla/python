class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0

        def longestPalindromeSubseq(s: str) -> int:
            dp = [[0 for j in range(len(s))] for i in range(len(s))]

            for i in reversed(range(len(s))):
                dp[i][i] = 1
                for j in range(i + 1, len(s)):
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i+1][j])

            return dp[0][len(s)-1]
        return len(s) - longestPalindromeSubseq(s) + 1
