from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0]*(target+1)

        for t in range(1, target+1):
            dp[t] = -1
            for i in range(9):
                if t >= cost[i]:
                    dp[t] = max(dp[t], 1 + dp[t - cost[i]])
            print(dp)

        if dp[t] < 0:
            return "0"

        res = []
        for i in range(8, -1, -1):
            while target >= cost[i] and dp[target] == 1 + dp[target - cost[i]]:
                res.append(1 + i)
                target -= cost[i]
        return ''.join(map(str, res))


cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
target = 9
s = Solution()
print(s.largestNumber(cost, target))
