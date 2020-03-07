from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def dfs(r, c, triangle, dp):
            if r == len(triangle):
                return 0
            if dp[r][c] != float('inf'):
                return dp[r][c]

            left = dfs(r+1, c, triangle, dp)
            right = dfs(r+1, c+1, triangle, dp)
            dp[r][c] = min(left, right) + triangle[r][c]
            return dp[r][c]

        rows = len(triangle)
        cols = len(triangle[rows-1])
        dp = [[float('inf')]*cols
              for _ in range(rows)]

        return dfs(0, 0, triangle, dp)


list = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
s = Solution()
print(s.minimumTotal(list))
