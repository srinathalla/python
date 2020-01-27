from typing import List


class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[n for j in arr] for i in arr]

        for i in range(len(arr)):
            dp[i][i] = 1

        for i in range(len(arr)-1):
            dp[i][i + 1] = 1 if arr[i] == arr[i+1] else 2

        for length in range(3, len(arr) + 1):
            for i in range(len(arr) - length + 1):
                j = i + length - 1

                if arr[i] == arr[j]:
                    dp[i][j] = dp[i+1][j-1]

                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

        return dp[0][len(arr)-1]


arr1 = [1, 3, 4, 1, 5]
s = Solution()
print(s.minimumMoves(arr1))
