from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        res = []
        n = len(matrix)
        m = len(matrix[0])

        av = [[False] * m for _ in range(n)]
        pv = [[False] * m for _ in range(n)]

        r = [0, 0, 1, -1]
        c = [1, -1, 0, 0]

        def dfs(i, j, v):
            if v[i][j] == True:
                return

            v[i][j] = True
            for k in range(4):
                ar = i + r[k]
                ac = j + c[k]
                if ar < 0 or ar >= n or ac < 0 or ac >= m or v[ar][ac] == True or matrix[ar][ac] < matrix[i][j]:
                    continue
                dfs(ar, ac, v)

        for i in range(n):
            dfs(i, 0, pv)
            dfs(i, m-1, av)

        for i in range(m):
            dfs(0, i, pv)
            dfs(n-1, i, av)

        for i in range(n):
            for j in range(m):
                if av[i][j] == True and pv[i][j] == True:
                    res.append([i, j])

        return res


s = Solution()

m = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(s.pacificAtlantic(m))
