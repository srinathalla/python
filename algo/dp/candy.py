from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        dp = [1 for i in ratings]

        prev = ratings[0]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                dp[i] = 1 + dp[i-1]

        for i in reversed(range(len(ratings)-1)):
            if ratings[i] > ratings[i+1]:
                dp[i] = max(dp[i], 1 + dp[i+1])

        return sum(dp)


s = Solution()
print(s.candy([1, 0, 2]))
print(s.candy([1, 2, 2]))
