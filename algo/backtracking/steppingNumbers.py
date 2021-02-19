from typing import List


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:

        res = []
        q = []
        for i in range(1, 10):
            q.append(i)
        if 0 >= low and 0 <= high:
            res.append(0)

        while q:
            p = q.pop(0)
            if p < high:
                r = p % 10
                if r > 0:
                    q.append(p * 10 + r - 1)
                if r < 9:
                    q.append(p * 10 + r + 1)

            if p >= low and p <= high:
                res.append(p)

        return res


s = Solution()
print(s.countSteppingNumbers(0, 21))
