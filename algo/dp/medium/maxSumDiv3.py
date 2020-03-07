from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0 for _ in range(3)]

        for no in nums:
            dp2 = dp[:]
            for p in dp:
                sum = p + no
                idx = sum % 3
                dp2[idx] = max(dp2[idx], sum)
            dp = dp2
        return dp[0]


s = Solution()
print(s.maxSumDivThree([3, 6, 5, 1, 8]))
