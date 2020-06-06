from typing import List


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        s = sum(A)
        dp = [[0]*(len(A)//2 + 1) for _ in range(s + 1)]
        dp[0][0] = True

        for no in A:
            for i in range(no, s + 1)[::-1]:
                for j in range(1, len(A)//2 + 1):
                    dp[i][j] = dp[i][j] or dp[i-no][j-1]
                    if dp[i][j]:
                        print("no:" + str(no) + "i:" + str(i) +
                              "j:" + str(j) + str(dp[i][j]))

        for i in range(1, len(A)//2 + 1):
            if (s*i) % len(A) == 0 and dp[s*i//len(A)][i]:
                return True

        return False


arr = [1, 2, 3, 4, 5, 6, 7, 8]
s = Solution()
print(s.splitArraySameAverage(arr))
