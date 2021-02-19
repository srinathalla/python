import collections
from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        cnt = 0
        pair = [-1] * n
        for x, y in pairs:
            pair[x] = y
            pair[y] = x

        pref = collections.defaultdict(lambda: {})

        for i, p in enumerate(preferences):
            for j, a in enumerate(p):
                pref[i][a] = j

        for x, p in enumerate(pair):
            for alt in preferences[x]:
                if p == alt:
                    break

                if pref[alt][x] < pref[alt][pair[alt]]:
                    cnt += 1
                    break
        return cnt


n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]

s = Solution()
print(s.unhappyFriends(n, preferences, pairs))
