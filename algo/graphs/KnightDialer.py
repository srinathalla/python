class Solution:
    def knightDialer(self, N: int) -> int:

        def recurse(N, i, j,  map, M):
            if i < 0 or i >= 4 or j < 0 or j >= 3 or (i == 3 and j != 1):
                return 0

            if N == 1:
                return 1
            if map.get((i, j, N), 0) > 0:
                return map[i, j, N]

            s = (recurse(N-1, i-1, j-2, map, M) % M
                 + recurse(N-1, i-1, j+2, map, M) % M
                 + recurse(N-1, i-2, j-1, map, M) % M
                 + recurse(N-1, i-2, j+1, map, M) % M
                 + recurse(N-1, i+1, j-2, map, M) % M
                 + recurse(N-1, i+1, j+2, map, M) % M
                 + recurse(N-1, i+2, j-1, map, M) % M
                 + recurse(N-1, i+2, j+1, map, M) % M)

            map[i, j, N] = s
            return map[i, j, N]

        sum = 0
        cache = {}
        M = 1000000007
        for i in range(4):
            for j in range(3):
                sum = (sum + recurse(N, i, j, cache, M) % M) % M
        return sum
