from typing import List

# T.C : O(logn) binary search for peak element


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l = 0
        r = len(A)-1

        while l < r:
            m = (l + r)//2

            if A[m] < A[m + 1]:
                l = m + 1
            else:
                r = m

        return l


s = Solution()
println(s.peakIndexInMountainArray([0, 2, 1, 0]))
