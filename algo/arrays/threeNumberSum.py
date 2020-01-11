from typing import List


def threeNumberSum(array, targetSum):
    array.sort()
    result = []

    for i in range(len(array)):
        itemsSet = set()
        newTargetSum = targetSum - array[i]
        for j in range(i+1, len(array)):
            if newTargetSum - array[j] in itemsSet:
                result.append([array[i], newTargetSum - array[j], array[j]])
            itemsSet.add(array[j])

    result.sort(key=lambda item: (item[0], item[1]))
    return result


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        prev = float('-inf')
        while i < len(nums) - 2:
            if nums[i] != prev:
                j = i + 1
                k = len(nums) - 1

                prevj = float('-inf')
                prevk = float('-inf')
                while j < k:

                    if nums[i] + nums[j] + nums[k] == 0:
                        if nums[j] != prevj and nums[k] != prevk:
                            result.append([nums[i], nums[j], nums[k]])

                        prevj = nums[j]
                        prevk = nums[k]
                        j += 1
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    else:
                        k -= 1

                prev = nums[i]
            i += 1
        return result


# print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))


s = Solution()

res = s.threeSum([-2, 0, 0, 2, 2])
print(res)
