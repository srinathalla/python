from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s = set()
        nums.sort()
        i = 0

        res = 0
        while i < len(nums):
            if nums[i] - k in s:
                res += 1
                while i < len(nums) - 1 and nums[i] == nums[i+1]:
                    i += 1

            s.add(nums[i])
            i += 1
        return res


s = Solution()
print(s.findPairs([1, 3, 1, 5, 4], 0))
