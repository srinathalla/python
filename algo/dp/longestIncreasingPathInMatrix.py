from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        res = float('-inf')
        prev = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dp[i][j] == 0:
                    self.dfs(matrix, i, j, dp, prev)
                    res = max(res, dp[i][j])

        return res

    def dfs(self, matrix: List[List[int]], i: int, j: int, dp: List[List[int]], prev: int) -> int:

        if i < 0 or i > (len(matrix) - 1) or j < 0 or j > (len(matrix[0]) - 1) or matrix[i][j] <= prev:
            return 0

        if dp[i][j] != 0:
            return dp[i][j]

        top = self.dfs(matrix, i + 1, j, dp, matrix[i][j])
        bottom = self.dfs(matrix, i - 1, j, dp, matrix[i][j])
        right = self.dfs(matrix, i, j + 1, dp, matrix[i][j])
        left = self.dfs(matrix, i, j - 1, dp, matrix[i][j])

        dp[i][j] = max(top, bottom, left, right) + 1
        print("dp[" + str(i) + "]" + "[" + str(j) + "] :" + str(dp[i][j]))

        return dp[i][j]


matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]]
s = Solution()
print(s.longestIncreasingPath(matrix))
