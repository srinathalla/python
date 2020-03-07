import collections
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = collections.Counter(s[i:i+10] for i in range(len(s) - 9))
        return [w for w in count if count[w] > 1]


s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

s = Solution()
print(s.findRepeatedDnaSequences(s1))
