from typing import List

#
# T.C : O(3n) => O(n)
# #


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        if len(nums) < 2:
            return

        i = len(nums) - 1
        # Traverse till you find an element not in descreasing sequence, lets say it is a
        # pivot element
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        j = i - 1
        # if entire array is in decreasing sequence, we need to make nums as increasing sequence.
        if j < 0:
            nums.reverse()
            return

        # find element which is higher than pivot element.
        i = len(nums) - 1
        while i >= 0 and nums[j] >= nums[i]:
            i -= 1

        # swap pivot element with next higher element
        tmp = nums[j]
        nums[j] = nums[i]
        nums[i] = tmp

        i = len(nums) - 1
        j += 1

        # reverse the decreasing sequence to make it increasing sequence to the right of pivot
        # element.
        while j < i:
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp
            i -= 1
            j += 1


s = Solution()
l = [1, 2, 3]
# s.nextPermutation(l)
print(l)

l = [3, 2, 1]
# s.nextPermutation(l)
print(l)

l = [1, 5, 1]
# s.nextPermutation(l)
print(l)

l = [1, 1]
s.nextPermutation(l)
print(l)
