#
# T.C : O(n + m) where n is length of biggest string, m is length of smallest string.
# S.C : O(m)
# #


def smallestSubstringContaining(bigString, smallString):

    charsCount = {}
    distinctCharsCount = 0
    for ch in smallString:
        if ch not in charsCount:
            charsCount[ch] = 0
            distinctCharsCount += 1
        charsCount[ch] += 1

    start = 0
    i = 0
    minLen = [0, len(bigString) + 1]
    distinctCharsInBigString = 0
    while i < len(bigString):
        key = bigString[i]
        if key in charsCount:
            charsCount[key] -= 1
            if charsCount[key] == 0:
                distinctCharsInBigString += 1

            while distinctCharsInBigString == distinctCharsCount:
                if minLen[1] - minLen[0] > i + 1 - start:
                    minLen[1] = i + 1
                    minLen[0] = start

                key = bigString[start]
                if key in charsCount:
                    charsCount[key] += 1
                    if charsCount[key] > 0:
                        distinctCharsInBigString -= 1

                start += 1
        i += 1

    return bigString[minLen[0]:minLen[1]] if minLen[1] < len(bigString) + 1 else ''


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        charsInT = {}
        required = 0
        for i in range(len(t)):
            if t[i] not in charsInT:
                charsInT[t[i]] = 0
                required += 1

            charsInT[t[i]] += 1

        charsInS = {}
        formed = 0

        left = 0
        minVal = [0, len(s) + 1]
        for i in range(len(s)):

            if s[i] not in charsInS:
                charsInS[s[i]] = 0

            charsInS[s[i]] += 1

            if s[i] in charsInT and charsInS[s[i]] == charsInT[s[i]]:
                formed += 1

            while required == formed:

                if minVal[1] - minVal[0] > i - left + 1:
                    minVal[1] = i + 1
                    minVal[0] = left

                charsInS[s[left]] -= 1
                if s[left] in charsInT and charsInS[s[left]] < charsInT[s[left]]:
                    formed -= 1

                left += 1

        return s[minVal[0]:minVal[1]] if minVal[1] != len(s) + 1 else ""


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
#print(s.minWindow("a", "b"))
print(s.minWindow("aab", "aab"))


bigString = "abcd$ef$axb$c$"
smallString = "$$abf"
expected = "f$axb$"

# print(smallestSubstringContaining(bigString, smallString))
