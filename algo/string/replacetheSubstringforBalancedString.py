import collections


class Solution:
    def balancedString(self, s):
        count = collections.Counter(s)
        j = 0
        res = len(s)
        n = len(s)

        for i, c in enumerate(s):
            count[c] -= 1
            while j < len(s) and all(count[ch] <= n//4 for ch in 'QWER'):
                res = min(res, i - j + 1)
                count[s[j]] += 1
                j += 1
        return res


s = Solution()
print
# print(s.balancedString("QQQW"))
print(s.balancedString("WWEQERQWQWWRWWERQWEQ"))
