import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ctr = collections.Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= collections.Counter(set(ctr))
        return [n for n in ctr if nums.count(n) > len(nums)/3]


nums = [1, 1, 1, 3, 3, 2, 2, 2]
s = Solution()
print(s.majorityElement(nums))
