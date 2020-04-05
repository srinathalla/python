from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        n = len(matrix)
        m = len(matrix[0])
        res = [[0 if matrix[i][j] == 0 else n * m +
                1 for j in range(m)] for i in range(n)]

        q = []

        for i in range(n):
            for j in range(m):
                if res[i][j] == 0:
                    q.append((i, j, 0))
        r = [0, 0, 1, -1]
        c = [1, -1, 0, 0]

        while len(q) > 0:
            item = q.pop(0)

            for i in range(4):
                ar = item[0] + r[i]
                ac = item[1] + c[i]
                cost = 1 + item[2]

                if ar >= 0 and ar < n and ac >= 0 and ac < m and res[ar][ac] == n*m + 1:
                    res[ar][ac] = cost
                    q.append((ar, ac, cost))
        return res


arr = [[0, 0, 0],
       [0, 1, 0],
       [1, 1, 1]]

s = Solution()
arr = s.updateMatrix(arr)
print(arr)
