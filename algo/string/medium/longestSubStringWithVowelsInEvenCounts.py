class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = 'aeiou'

        P = [0]
        for c in s:
            if c in vowels:
                i = vowels.index(c)
                mask = 1 << i
                P.append(P[-1] ^ mask)
            else:
                P.append(P[-1])

        first = [None] * 32
        last = [None] * 32
        for i, x in enumerate(P):
            if first[x] is None:
                first[x] = i
            last[x] = i

        ans = 0
        for i in range(32):
            if first[i] is not None:
                ans = max(ans, last[i] - first[i])
        return ans


s = Solution()
print(s.findTheLongestSubstring("eleetminicoworoep"))
