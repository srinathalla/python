from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        if len(nums) < 2:
            return False

        k = abs(k)
        map = {}
        map[0] = -1
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

            if k > 0:
                sum = sum % k

            if sum in map:
                if i - map[sum] > 1:
                    return True
            else:
                map[sum] = i

        return False


print()
