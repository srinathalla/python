from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [1 for _ in range(len(arr))]

        maxVal = 1
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] - arr[j] == difference:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxVal = max(maxVal, dp[i])

        return maxVal


arr = [1, 2, 3, 4]
difference = 1
s = Solution()
print(s.longestSubsequence(arr, difference))
