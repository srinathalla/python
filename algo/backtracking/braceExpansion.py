from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        self.res = []

        def helper(s, word):
            if not s:
                self.res.append(word)

            else:
                if s[0] == "{":
                    i = s.find("}")
                    for l in s[1:i].split(','):
                        helper(s[i+1:], word + l)
                else:
                    helper(s[1:], word + s[0])

        helper(s, "")
        self.res.sort()
        return self.res


s = Solution()
print(s.expand("{a,b}c{d,e}f"))
