from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:

        res = []
        res.append(0)
        for i in range(n):
            size = len(res)
            for k in range(size-1, -1, -1):
                res.append(res[k] | 1 << i)

        return res


s = Solution()
print(s.grayCode(3))
