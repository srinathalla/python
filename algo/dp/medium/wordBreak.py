from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordDict = set(wordDict)

        @lru_cache(None)
        def wb(i):
            if i == len(s):
                return []

            if s[i:] in wordDict:
                return [s[i:]]
            res = []
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr in wordDict:
                    ret = wb(j+1)

                    for rw in ret:
                        res.append(substr + " " + rw)
            return res

        return wb(0)


st = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s = Solution()
print(s.wordBreak(st, wordDict))
