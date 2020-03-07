from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        count = [1 for _ in range(len(nums))]
        seq = [-1 for _ in range(len(nums))]
        maxV = 0
        idx = -1
        for i in range(1, len(nums)):

            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if count[i] < count[j] + 1:
                        count[i] = count[j] + 1
                        seq[i] = j

            if count[i] > maxV:
                maxV = count[i]
                idx = i

        result = []

        while idx != -1:
            result.insert(0, nums[idx])
            idx = seq[idx]
        return result


s = Solution()
print(s.largestDivisibleSubset([1, 2, 3]))
