class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2:
            return

        i = len(nums) - 1
        while i > 0 and nums[i-1] > nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return

        j = i - 1
        i = len(nums) - 1
        while nums[j] >= nums[i]:
            i -= 1

        tmp = nums[j]
        nums[j] = nums[i]
        nums[i] = tmp

        i = len(nums) - 1
        j += 1

        while j < i:
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp
            j += 1
            i -= 1
