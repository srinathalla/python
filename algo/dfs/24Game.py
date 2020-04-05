from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:

        eps = 0.001

        def dfs(items):
            if len(items) == 1:
                return True if abs(items[0] - 24) < eps else False

            for i in range(len(items)):
                for j in range(i+1, len(items)):
                    for c in compute(items[i], items[j]):
                        nextR = []
                        nextR.append(c)

                        for k in range(len(items)):
                            if k == i or k == j:
                                continue
                            nextR.append(items[k])
                        if dfs(nextR):
                            return True
            return False

        def compute(a, b):
            c = [a+b, a-b, b-a, a*b]
            if b != 0:
                c.append(a/b)
            if a != 0:
                c.append(b/a)
            return c

        return dfs(nums)


s = Solution()
print(s.judgePoint24([1, 2, 1, 2]))
