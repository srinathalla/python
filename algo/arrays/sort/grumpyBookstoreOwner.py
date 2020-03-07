from typing import List


class Solution:
    def maxSatisfied(self, cust: List[int], grumpy: List[int], X: int) -> int:

        satisfied = 0
        max_make_satisfied = 0
        curr_make_satisfied = 0
        i = 0
        for c, g in zip(cust, grumpy):
            satisfied += c * (1 - g)
            curr_make_satisfied += g*c
            if i >= X:
                curr_make_satisfied -= cust[i-X] * grumpy[i-X]

            max_make_satisfied = max(max_make_satisfied, curr_make_satisfied)
            i += 1

        return satisfied + max_make_satisfied


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3

s = Solution()
# print(s.maxSatisfied(customers, grumpy, X))

c = [4, 10, 10]
g = [1, 1, 0]
X = 2
print(s.maxSatisfied(c, g, X))
