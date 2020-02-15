class Solution:
    def superEggDropRecursive(self, k: int, n: int) -> int:
        if n <= 1:
            return n

        if k == 1:
            return n

        minVal = float('inf')
        for i in range(1, n + 1):
            res = 1 + min(self.superEggDrop(k-1, i-1),
                          self.superEggDrop(k, n-i))
            minVal = min(minVal, res)

        return minVal

    def superEggDropBruteForce(self, k: int, n: int) -> int:
        table = [[0 for _ in range(n+1)] for _ in range(k+1)]

        for i in range(k+1):
            table[i][0] = 0
            table[i][1] = 1

        for i in range(2, n+1):
            table[1][i] = i

        for i in range(2, k+1):
            for j in range(2, n+1):
                minV = float('inf')
                for x in range(1, j+1):
                    res = 1 + max(table[i-1][x-1], table[i][j-x])
                    minV = min(minV, res)
                table[i][j] = minV

        return table[k][n]

    def superEggDrop(self, k: int, n: int):
        dp = [[0]*(k+1) for _ in range(n+1)]
        m = 0
        while dp[m][k] < n:
            m += 1
            for j in range(1, k+1):
                dp[m][k] = dp[m-1][j-1] + dp[m-1][j] + 1
        return m


s = Solution()
print(s.superEggDrop(1, 2))
print(s.superEggDrop(1, 3))
