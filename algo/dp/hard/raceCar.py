class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        for i in range(1, target+1):
            m = 1
            j = 1

            dp[i] = float('inf')
            while j < i:
                q = 0
                p = 0
                while p < j:
                    dp[i] = min(dp[i], m + 1 + q + 1 + dp[i-(j-p)])
                    q += 1
                    p = (1 << q) - 1

                m += 1
                j = (1 << m) - 1

            dp[i] = min(dp[i], m + (0 if i == j else dp[j-i] + 1))

        return dp[target]
