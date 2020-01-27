class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def longestPalidromeSubSequence(s: str):
            dp = [[0 for j in range(len(s))] for i in range(len(s))]

            for i in reversed(range(len(s))):
                dp[i][i] = 1
                for j in range(i+1, len(s)):
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i+1][j])
            return dp[0][len(s)-1]

        return len(s) - longestPalidromeSubSequence(s) <= k


s = Solution()
print(s.isValidPalindrome("abcdeca", 2))
