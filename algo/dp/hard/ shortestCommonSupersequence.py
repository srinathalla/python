class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n, m = len(str1), len(str2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):

                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j])

        result = []
        i = n
        j = m

        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result.insert(0, str1[i-1])
                i -= 1
                j -= 1
            else:
                if dp[i][j] - 1 == dp[i][j-1]:
                    result.insert(0, str2[j-1])
                    j -= 1
                else:
                    result.insert(0, str1[i-1])
                    i -= 1

        while j > 0:
            result.insert(0, str2[j-1])
            j -= 1
        while i > 0:
            result.insert(0, str1[i-1])
            i -= 1

        return ''.join(result)


str1 = "abac"
str2 = "cab"
s = Solution()
print(s.shortestCommonSupersequence(str1, str2))
