from typing import List

#
# T.C : O(2nlogn) => O(nlogn)
# #


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.search(nums, target, True)
        right = self.search(nums, target, False)

        return [left, right]

    def search(self, nums: List[int], target: int, isLeft: bool) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r)//2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                if isLeft:
                    if m == 0 or (m > 0 and nums[m-1] != target):
                        return m
                    else:
                        r = m - 1
                else:
                    if m == len(nums) - 1 or (m < len(nums) - 1 and nums[m+1] != target):
                        return m
                    else:
                        l = m + 1

        return -1


s = Solution()

print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
