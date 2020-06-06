from typing import List
import bisect
from collections import Counter


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        wf = []
        for w in words:
            cnt = Counter(w)
            wf.append(cnt[min(w)])
        wf.sort()

        qf = []
        for q in queries:
            cnt = Counter(q)
            qf.append(cnt[min(q)])

        tot = 0
        res = []
        for v in qf:
            idx = bisect.bisect_right(wf, v)
            res.append(len(wf) - idx)
        return res


s = Solution()
print(s.numSmallerByFrequency(["bbb", "cc"], ["a", "aa", "aaa", "aaaa"]))
