class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = [0 for _ in range(26)]
        maxLen = 0
        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i-1]) - ord(p[i]) == 25):
                maxLen += 1
            else:
                maxLen = 1
            idx = ord(p[i]) - ord('a')
            dp[idx] = max(dp[idx], maxLen)

        return sum(dp)


s = Solution()
print(s.findSubstringInWraproundString("zab"))
