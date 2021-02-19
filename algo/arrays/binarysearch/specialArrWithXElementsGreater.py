from typing import List
import bisect


class Solution:
    def specialArray(self, nums: List[int]) -> int:

        nums.sort()

        for i in range(0, 1001):
            pos = bisect.bisect_left(nums, i)

            if len(nums) - pos == i:
                return i

        return -1


arr = [3, 5]
s = Solution()
print(s.specialArray([0, 4, 3, 0, 4]))
