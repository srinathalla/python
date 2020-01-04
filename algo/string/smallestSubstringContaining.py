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


# print(smallestSubstringContaining("abcdef", "fa"))

bigString = "abcd$ef$axb$c$"
smallString = "$$abf"
expected = "f$axb$"

print(smallestSubstringContaining(bigString, smallString))
