from typing import List


class Solution:
    def solve(self, b: List[List[str]]) -> None:

        n = len(b)
        if n < 2:
            return
        m = len(b[0])

        for i in range(1, n-1):
            for j in range(1, m-1):
                if b[i][j] == 'O':
                    if (b[i+1][j] == 'O' and i + 1 == n-1) or (b[i - 1][j] == 'O' and i - 1 == 0) or (b[i][j+1] == 'O' and j + 1 == m-1) or (b[i][j-1] == 'O' and j - 1 == 0):
                        continue

                    b[i][j] = 'X'


g = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
     ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
s = Solution()
s.solve(g)
print(g)
