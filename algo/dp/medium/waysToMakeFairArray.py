from typing import List


class Solution:
    def waysToMakeFair(self, A: List[int]) -> int:
        s1, s2 = [0, 0], [sum(A[0::2]), sum(A[1::2])]
        res = 0
        for i, a in enumerate(A):
            s2[i % 2] -= a
            res += s1[0] + s2[1] == s1[1] + s2[0]
            s1[i % 2] += a
        return res


s = Solution()
nums = [2, 1, 6, 4]
print(s.waysToMakeFair(nums))
