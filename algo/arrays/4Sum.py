from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j] != nums[j-1]:
                        k = j + 1
                        l = len(nums) - 1
                        while k < l:
                            if nums[i] + nums[j] + nums[k] + nums[l] == target:
                                res.append(
                                    [nums[i], nums[j], nums[k], nums[l]])
                                while k < l and nums[k] == nums[k+1]:
                                    k += 1
                                while k < l and nums[l] == nums[l-1]:
                                    l -= 1
                                k += 1
                                l -= 1
                            elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                                l -= 1
                            else:
                                k += 1
        return res


s = Solution()
#print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s.fourSum([0, 0, 0, 0], 0))
