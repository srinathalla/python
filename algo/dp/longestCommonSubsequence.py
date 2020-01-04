def longestCommonSubsequenceWithRecursion(str1, str2):
    return recurse(str1, str2, len(str1) - 1, len(str2) - 1)

def recurse(str1, str2, i, j):
    if i < 0 or j < 0:
        return 0

    if str1[i] == str2[j]:
        return 1 + recurse(str1, str2, i-1, j-1)
    else:
        return max(recurse(str1, str2, i-1, j), recurse(str1, str2, i, j-1))
#
# T.C : O(n*m) , S.C O(n*m)
# 
# #
def longestCommonSubsequence(str1, str2):
    table = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(1,len(str1) +1):
        for j in range(1,len(str2) +1):
            if str1[i-1] == str2[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i][j-1],table[i-1][j])
    
    return getSequence(table,str1,str2)

def getSequence(table,str1,str2):
    i = len(str1)
    j = len(str2)
    sequence = []
    while (i > 0 and j > 0):
        if table[i][j] == table[i][j-1] or table[i][j] == table[i-1][j]:
            if table[i][j] == table[i][j-1]:
                j -=1
            else:
                i -=1
        else:
            sequence.insert(0,str1[i-1])
            i -=1
            j -=1
    return sequence


seq = longestCommonSubsequence("", "")
print(*seq)

seq = longestCommonSubsequence("ZXVVYZW", "XKYKZPW")
print(*seq)
