from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(self.robHouse(nums, 0, len(nums) - 2), self.robHouse(nums, 1, len(nums) - 1))

    def robHouse(self, nums: List[int], low, high) -> int:

        nums = nums[low:high+1]
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n-1]


nums = [1, 2, 3, 1]

s = Solution()
# print(s.rob(nums))
nums = [1, 2, 1, 1]
print(s.rob(nums))
print(s.rob([0, 0]))
