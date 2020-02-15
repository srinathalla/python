class Solution:
    def numDecodings(self, s: str) -> int:

        if s is None or len(s) == 0:
            return 0

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s) + 1):
            no = int(s[i-1])
            if no >= 1 and no <= 9:
                dp[i] += dp[i-1]

            no = int(s[i-2:i])
            if no >= 10 and no <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]


s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("226"))
