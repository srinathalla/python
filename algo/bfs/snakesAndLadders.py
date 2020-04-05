from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        arr = []
        ltr = True
        for i in range(n)[::-1]:
            row = board[i]
            if ltr:
                arr = arr + row
            else:
                arr = arr + row[::-1]
            ltr = not ltr

        start = 0 if arr[0] == -1 else arr[0]
        visited = [False] * (n*n)
        visited[start] = True

        q = []
        q.append(start)

        steps = 0
        while q:

            s = len(q)
            for i in range(s):
                v = q.pop(0)

                if v == n*n - 1:
                    return steps
                for j in range(1, 7):
                    av = v + j
                    if av >= n * n:
                        continue
                    if arr[av] != -1:
                        av = arr[av] - 1

                    if visited[av] == False:
                        visited[av] = True
                        q.append(av)
            steps += 1
        return -1


s = Solution()
g = [[1, 1, -1], [1, 1, 1], [-1, 1, 1]]


print(s.snakesAndLadders(g))
