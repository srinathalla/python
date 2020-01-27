from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > 0 and i > 0 and j > 0:
                    matrix[i][j] = min(
                        matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                ans += matrix[i][j]

        return ans


matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]]

s = Solution()
print(s.countSquares(matrix))
