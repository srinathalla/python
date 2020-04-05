from typing import List
import collections


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        map = {}

        for b in B:
            count = collections.Counter(b)
            for v in count:
                if v not in map:
                    map[v] = count[v]
                else:
                    map[v] = max(map[v], count[v])

        res = []
        for a in A:
            ac = collections.Counter(a)
            subset = True
            for key in map.keys():
                if key not in ac or map[key] > ac[key]:
                    subset = False
                    break

            if subset:
                res.append(a)
        return res


A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["lo", "eo"]
s = Solution()
print(s.wordSubsets(A, B))
