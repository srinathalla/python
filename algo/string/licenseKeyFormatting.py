from typing import List


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        S = S.upper()
        S = S.replace('-', '')
        k = 0

        fs = []
        for i in reversed(range(len(S))):
            fs.insert(0, S[i])
            k += 1

            if k % K == 0:
                fs.insert(0, '-')

        if fs[0] == '-':
            fs = fs[1:]

        return ''.join(fs)


s = Solution()
S = "5F3Z-2e-9-w"
K = 4
print(s.licenseKeyFormatting(S, K))
