from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        n = len(nums)
        cnt = [0] * n

        nums.sort()
        mod = 10**9 + 7

        for s, e in requests:
            cnt[s] += 1
            if e + 1 < n:
                cnt[e+1] -= 1

        for i in range(1, n):
            cnt[i] += cnt[i-1]

        cnt.sort()

        res = 0
        for i in range(n):
            res = (res + cnt[i] * nums[i]) % mod

        return res


nums = [1, 2, 3, 4, 5]
req = [[1, 3], [0, 1]]
s = Solution()
print(s.maxSumRangeQuery(nums, req))
