from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [num for num in nums]
        arr.insert(0, 1)
        arr.append(1)
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for gap in range(2, n):
            for left in range(n - gap):
                curr = 0
                right = left + gap
                for mid in range(left + 1, right):
                    curr = max(
                        curr, (dp[left][mid] + dp[mid][right] + (arr[left]*arr[mid]*arr[right])))
                dp[left][right] = curr

        return dp[0][len(arr)-1]


s = Solution()
print(s.maxCoins([3, 1]))
