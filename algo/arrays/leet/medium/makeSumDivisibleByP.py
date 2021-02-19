from typing import List


class Solution:
    def minSubarray(self, A: List[int], p: int) -> int:

        need = sum(A) % p
        dp = {0: -1}
        cur = 0
        res = n = len(A)
        for i, a in enumerate(A):
            cur = (cur + a) % p
            dp[cur] = i
            if (cur - need + p) % p in dp:
                res = min(res, i - dp[(cur - need + p) % p])
        return res if res < n else -1


nums = [3, 1, 4, 2]
p = 6
s = Solution()
#print(s.minSubarray(nums, p))
nums1 = [26, 19, 11, 14, 18, 4, 7, 1, 30, 23, 19, 8, 10, 6, 26, 3]
p1 = 26
print(s.minSubarray(nums1, p1))
