import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)

        print([left, right])

        return [-1, -1] if left == right else [left, right - 1]


nums = [5, 7, 7, 8, 8, 10]
target = 6
s = Solution()
print(s.searchRange(nums, target))
