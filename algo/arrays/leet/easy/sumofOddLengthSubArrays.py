from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        n = len(arr)
        ps = [0] * (n + 1)

        for i in range(n):
            ps[i+1] = ps[i] + arr[i]

        s = 0
        for i in range(n):
            for j in range(i, n):
                if (j-i + 1) % 2 == 1:
                    s += ps[j+1] - ps[i]
        return s


s = Solution()
arr = [1, 4, 2, 5, 3]
print(s.sumOddLengthSubarrays(arr))
