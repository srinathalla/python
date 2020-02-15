class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        p = 0
        s = 0
        match = -1
        starIdx = -1

        while s < len(text):

            if p < len(pattern) and (text[s] == pattern[p] or pattern[p] == '?'):
                s += 1
                p += 1

            elif p < len(pattern) and pattern[p] == '*':
                starIdx = p
                match = s
                p += 1

            elif starIdx >= 0:
                p = starIdx + 1
                match += 1
                s = match
            else:
                return False

        while p < len(pattern) and pattern[p] == '*':
            p += 1

        return p == len(pattern)


s = Solution()
# print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "*"))
print(s.isMatch("adceb", "a*b"))
