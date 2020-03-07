from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:

        m = len(A)
        n = len(A[0])
        res = n - 1
        dp = [1]*n

        for i in range(1, n):
            for j in range(i):
                if all(entry[j] <= entry[i] for entry in A):
                    dp[i] = max(dp[i], dp[j] + 1)

            res = min(res, n - dp[i])

        return res


s = Solution()
print(s.minDeletionSize(["ghi", "def", "abc"]))
print(s.minDeletionSize(["babca", "bbazb"]))
print(s.minDeletionSize(["edcba"]))
