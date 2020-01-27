class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1

        v = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        while i < j:
            while i < len(s) and s[i] not in v:
                i += 1

            while j >= 0 and s[j] not in v:
                j -= 1

            if i < j:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp

            i += 1
            j -= 1

        return ''.join(s)


s = Solution()
print(s.reverseVowels("leetcode"))
