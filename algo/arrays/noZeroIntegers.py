from typing import List

#
# T.C : O(n)
# #


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        for i in range(1, n):
            if '0' not in f'{i}{n-i}':
                return [i, n-i]


s = Solution()

print(s.getNoZeroIntegers(1010))
print(s.getNoZeroIntegers(69))
print(s.getNoZeroIntegers(10000))
