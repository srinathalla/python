#
# T.C : O(2n) S.C O(n)
# #


def longestSubstringWithoutDuplication(string):
    if len(string) <= 1:
        return string

    i = 0
    start = 0
    lastSeen = {}

    maxPos = [0, 1]
    for i in range(len(string)):
        if string[i] in lastSeen:
            start = max(start, lastSeen[string[i]] + 1)

        if i + 1 - start > maxPos[1] - maxPos[0]:
            maxPos[1] = i + 1
            maxPos[0] = start

        lastSeen[string[i]] = i

    return string[maxPos[0]:maxPos[1]]

# O(n^2)


def longestSubstringWithoutDuplicationNaive(string):

    max = [0, 1]
    seen = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[j] in seen:
                j -= 1
                break
            seen.add(string[j])
        seen.clear()
        if j + 1 - i > max[1] - max[0]:
            max[1] = j + 1
            max[0] = i
    return string[max[0]: max[1]]


print(longestSubstringWithoutDuplication("abcdeabcdefc"))

print(longestSubstringWithoutDuplication("abc"))

# print(longestSubstringWithoutDuplicationNaive("abcdeabcdefc"))

print(longestSubstringWithoutDuplicationNaive("abc"))
