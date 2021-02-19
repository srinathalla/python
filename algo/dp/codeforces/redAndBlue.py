from functools import lru_cache


def rnb(r, b, m, n):

    @lru_cache(None)
    def dp(i, j):
        if i >= m and j >= n:
            return 0

        s1, s2 = 0, 0
        if i < m and j < n:
            return max(0, r[i] + dp(i+1, j), b[j] + dp(i, j+1))
        elif i < m:
            return max(0, r[i] + dp(i+1, j))
        else:
            return max(0, b[j] + dp(i, j+1))

    return dp(0, 0)


tc = int(input())

for i in range(tc):
    n = int(input())
    rs = input()
    rsarr = rs.split(" ")
    rsarr = list(map(int, rsarr))
    m = int(input())
    bs = input()
    bsarr = bs.split(" ")
    bsarr = list(map(int, bsarr))
    print(rnb(rsarr, bsarr, n, m))
