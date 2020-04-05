from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        c = Counter(p)

        sc = Counter()
        begin = 0
        end = 0

        res = []
        while end < len(s):
            sc[s[end]] += 1

            if end - begin + 1 == len(p):
                if sc == c:
                    res.append(begin)

                sc[s[begin]] -= 1
                if sc[s[begin]] == 0:
                    del sc[s[begin]]
                begin += 1

            end += 1
        return res


s = "cbaebabacd"
p = "abc"
sol = Solution()
print(sol.findAnagrams(s, p))
