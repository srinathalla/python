#
# T.C : O(n^3) + O(n^2) => O(n^3)
# S.C : O(n^2) + O(n) => O(n^2)
# #


def palindromePartitioningMinCutsNaive(string):
    palindromes = [[False for j in string] for i in string]

    for i in range(len(string)):
        for j in range(i, len(string)):
            palindromes[i][j] = isPalindrome(string, i, j)

    cuts = [i for i in range(len(string))]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i-1] + 1
            for j in range(0, i + 1):
                if palindromes[j][i]:
                    cuts[i] = min(cuts[i], cuts[j-1] + 1)

    return cuts[len(string) - 1]


def isPalindrome(string, i, j):
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

#
# T.C : O(n^2) S.C : O(n^2)
# #


def palindromePartitioningMinCuts(string):
    palindromes = [[False for j in string] for i in string]

    for i in range(len(string)):
        palindromes[i][i] = True

    for length in range(2, len(string) + 1):
        for i in range(len(string) - length + 1):
            j = i + length - 1
            if length == 2:
                palindromes[i][j] = string[i] == string[j]
            else:
                palindromes[i][j] = string[i] == string[j] and palindromes[i + 1][j-1]

    cuts = [i for i in range(len(string))]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i-1] + 1
            for j in range(0, i + 1):
                if palindromes[j][i]:
                    cuts[i] = min(cuts[i], cuts[j-1] + 1)

    return cuts[len(string) - 1]


print(palindromePartitioningMinCuts("noonabbad"))
