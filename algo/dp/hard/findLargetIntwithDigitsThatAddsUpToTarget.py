from typing import List
from functools import lru_cache


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:

        @lru_cache(None)
        def dp(ctarget):

            if ctarget == 0:
                return ""

            if ctarget < 0:
                return "0"

            res = "0"
            for i, c in enumerate(cost):
                ret = dp(ctarget-c)
                if ret != "0":
                    print(res)
                    res = max([res, str(i+1) + ret, ret + str(i+1)],
                              key=lambda x: len(x))
                    print(res)

            return res

        return dp(target)


s = Solution()
cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
target = 9

print(max(["0", "12", "21"], key=lambda x: len(x)))
#print(s.largestNumber(cost, target))
