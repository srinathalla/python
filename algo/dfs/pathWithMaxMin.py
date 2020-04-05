from typing import List


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:

        self.max = 0
        self.min = A[0][0]

        def dfs(i, j, arr):
            if i >= 0 and i < len(A) and j >= 0 and j < len(A[0]) and A[i][j] >= 0:
                if i == len(A) - 1 and j == len(A[0]) - 1:
                    self.max = max(self.max, min(arr))
                    return

                arr.append(A[i][j])
                A[i][j] = -1
                dfs(i+1, j, arr)
                dfs(i-1, j, arr)
                dfs(i, j + 1, arr)
                dfs(i, j - 1, arr)
                A[i][j] = arr.pop()

        dfs(0, 0, [])
        return self.max


g = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]
s = Solution()
print(s.maximumMinimumPath(g))
