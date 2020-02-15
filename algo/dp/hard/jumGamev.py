from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [0 for _ in range(len(arr))]

        def dfs(i, d, arr, dp):
            if dp[i] > 0:
                return dp[i]
            res = 1
            for j in range(i + 1, min(i+d, len(arr))):
                if arr[j] < arr[i]:
                    res = max(res, 1 + dfs(j, d, arr, dp))
                else:
                    break
            for j in reversed(range(max(0, i-d), i-1)):
                if arr[j] < arr[i]:
                    res = max(res, 1 + dfs(j, d, arr, dp))

            return res

        res = 1
        for i in range(len(arr)):
            res = max(res, dfs(i, d, arr, dp))

        return res


s = Solution()
print(s.maxJumps([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2))
