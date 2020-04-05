from typing import List


class Solution:
    def removeStones(self, points: List[List[int]]) -> int:
        UF = {}

        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for i, j in points:
            union(i, ~j)
        return len(points) - len({find(x) for x in UF})


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]

s = Solution()
print(s.removeStones(stones))
