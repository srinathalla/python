from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if grid[0][0] == 1:
            return -1

        visited = [[False] * m for _ in range(n)]
        q = []
        q.append((0, 0, 1))
        visited[0][0] = True

        r = [0, 0, 1, 1, 1, -1, -1, -1]
        c = [1, -1, 0, 1, -1, 0, 1, -1]

        while len(q) > 0:
            item = q.pop(0)
            if item[0] == n-1 and item[1] == m-1:
                return item[2]

            for i in range(8):
                adjr = item[0] + r[i]
                adjc = item[1] + c[i]
                cost = item[2] + 1

                if adjr >= 0 and adjr < n and adjc >= 0 and adjc < m and grid[adjr][adjc] == 0 and visited[adjr][adjc] == False:
                    q.append((adjr, adjc, cost))
                    visited[adjr][adjc] = True
        return -1


g = [[0, 0, 0], [1, 1, 0], [1, 1, 1]]
s = Solution()
print(s.shortestPathBinaryMatrix(g))
