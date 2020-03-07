import collections
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        keys = sorted(count.keys())

        for key in keys:
            if count[key] > 0:
                kc = count[key]
                for i in range(key, key + k):
                    if count[i] < kc:
                        return False
                    count[i] -= kc
        return True


nums = [1, 2, 3, 4]
k = 3
s = Solution()
print(s.isPossibleDivide(nums, k))
