from typing import List


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:

        def dfs(A, i, j):
            if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] != 1:
                return

            A[i][j] = 2
            dfs(A, i+1, j)
            dfs(A, i-1, j)
            dfs(A, i, j + 1)
            dfs(A, i, j - 1)

        def expand(A, i, j, v):
            if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
                return False
            if A[i][j] == 0:
                A[i][j] = v + 1

            return A[i][j] == 1

        found = False
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    dfs(A, i, j)
                    found = True
                    break
            if found:
                break

        c = 2
        while True:
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j] == c and (expand(A, i+1, j, c) or expand(A, i-1, j, c) or expand(A, i, j + 1, c) or expand(A, i, j - 1, c)):
                        return c - 2
            c += 1


A = [[0, 1], [1, 0]]
s = Solution()
print(s.shortestBridge(A))
