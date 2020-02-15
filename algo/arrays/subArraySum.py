from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        map = {}
        map[0] = 1
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if (sum - k) in map:
                count += map[sum-k]

            if sum not in map:
                map[sum] = 0
            map[sum] += 1

        return count


s = Solution()
print(s.subarraySum([1, 2, 1, 2, 1], 3))
