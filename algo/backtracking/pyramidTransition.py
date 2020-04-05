from collections import defaultdict
import itertools
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        f = defaultdict(set)
        for s in allowed:
            f[s[:2]].add(s[2:])

        def dfs(row, next, map, i):
            if len(row) == 1:
                return True
            if len(next) + 1 == len(row):
                return dfs(next, "", map, 1)

            for c in map.get(row[i-1:i+1], set()):
                if dfs(row, next + c, map, i + 1):
                    return True
            return False
        return dfs(bottom, "", f, 1)


bottom = "AABA"
allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]

s = Solution()
print(s.pyramidTransition(bottom, allowed))
