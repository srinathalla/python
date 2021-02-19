from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def getHash(input):
            start = ord(input[0]) - ord('a')

            res = []
            for c in input:
                val = ord(c) - start
                val = val + 26 if val < ord('a') else val
                res.append(chr(val))

            return ''.join(res)

        gmap = defaultdict(list)
        for st in strings:
            h = getHash(st)
            gmap[h].append(st)

        return list(gmap.values())


sol = Solution()
arr = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(sol.groupStrings(arr))
