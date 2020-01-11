from typing import List

#
# Idea is to transpose the matrix and reverse elements in each row.
# T.C : O(2*n*n) => O(n*n)
# S.C : O(1)
# #


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Transpose of a matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # reverse elements in each row
        for i in range(len(matrix)):
            j = 0
            k = len(matrix[0]) - 1

            while j < k:
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][k]
                matrix[i][k] = tmp
                j += 1
                k -= 1


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

s = Solution()
s.rotate(matrix)
print(matrix)
