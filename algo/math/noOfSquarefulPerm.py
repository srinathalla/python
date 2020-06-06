import collections
from typing import List


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        c = collections.Counter(A)
        cand = {i: {j for j in c if int(
            (i + j)**0.5) ** 2 == i + j} for i in c}

        def dfs(x, left=len(A) - 1):
            c[x] -= 1

            print("x: " + str(x) + " left: " + str(left))
            count = 0
            if left == 0:
                count += 1
            else:
                for y in cand[x]:
                    if c[y]:
                        count += dfs(y, left - 1)

            c[x] += 1
            return count
        return sum(map(dfs, c))


s = Solution()
print(s.numSquarefulPerms([1, 17, 8]))
