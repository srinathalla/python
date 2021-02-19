from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:

        n = len(seats)
        m = len(seats[0])
        v = [0] * n

        for i in range(n):
            for j in range(m):
                v[i] = (v[i] << 1) + (seats[i][j] == '.')

        stateSize = 1 << m

        dp = [[-1] * stateSize for _ in range(n)]

        def bc(a):
            if a <= 1:
                return a

            return bc(a//2) + (a % 2 == 1)

        for i in range(n):
            for j in range(stateSize):
                if (j & (j >> 1)) == 0 and (j & v[i]) == j:
                    if i == 0:
                        dp[i][j] = bc(j)
                    else:
                        for k in range(stateSize):
                            if (j & (k >> 1)) == 0 and (k & (j >> 1)) == 0 and dp[i-1][k] != -1:

                                dp[i][j] = max(dp[i][j], dp[i-1][k] + bc(j))

        return max(dp[-1])


seats = [["#", ".", "#", "#", ".", "#"],
         [".", "#", "#", "#", "#", "."],
         ["#", ".", "#", "#", ".", "#"]]

s = Solution()
print(s.maxStudents(seats))
