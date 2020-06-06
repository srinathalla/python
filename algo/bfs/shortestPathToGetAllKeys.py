from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        n = len(grid)
        m = len(grid[0])
        x = -1
        y = -1
        mk = -1
        for i in range(n):
            for j in range(m):
                ch = grid[i][j]
                if ch == '@':
                    x = i
                    y = j
                elif ord('a') <= ord(ch) <= ord('f'):
                    mk = max(mk, ord(ch) - ord('a') + 1)

        q = [(0, x, y)]
        visited = set()
        visited.add((0, x, y))

        row = [0, 0, -1, 1]
        col = [1, -1, 0, 0]

        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                keys, i, j = q.pop(0)
                if keys == (1 << mk) - 1:
                    return steps
                for k in range(4):
                    ar = i + row[k]
                    ac = j + col[k]
                    ak = keys
                    if 0 <= ar < n and 0 <= ac < m:
                        ch = grid[ar][ac]
                        if ord('a') <= ord(ch) <= ord('f'):
                            ak |= 1 << (ord(ch) - ord('a'))

                        if ord('A') <= ord(ch) <= ord('F'):
                            if (ak >> (ord(ch) - ord('A'))) & 1 == 0:
                                continue

                        if (ak, ar, ac) in visited or ch == '#':
                            continue

                        visited.add((ak, ar, ac))
                        q.append((ak, ar, ac))
            steps += 1
        return -1


s = Solution()
print(s.shortestPathAllKeys(["...#.", "a..@.", "#..#.", "b.#B.", ".##.A"]))
