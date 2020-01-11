from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        curr = lower
        result = []
        for no in nums:
            if curr < no:
                self.appendRange(result, curr, no-1)
            curr = no + 1
            if curr > upper:
                break

        if curr <= upper:
            self.appendRange(result, curr, upper)

        return result

    def appendRange(self, result, lower, upper):
        result.append(str(lower) + "->" + str(upper)
                      if lower != upper else str(lower))


s = Solution()
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
# print(s.findMissingRanges(nums, lower, upper))


# print(s.findMissingRanges([], 1, 1))


# print(s.findMissingRanges([1, 1, 1], 1, 1))


print(s.findMissingRanges([-2147483648, -2147483648,
                           0, 2147483647, 2147483647], -2147483648, 2147483647))
