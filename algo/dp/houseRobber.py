from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            max(nums[0], nums[1])

        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        print(dp)
        return dp[len(nums)-1]


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))
