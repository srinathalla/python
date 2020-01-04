#
# T.C : O(n*n*m + nlogn)
# S.C : O(n)
# where n : no of strings and m : length of longest string
# #
def longestStringChain(strings):
    strings.sort(key = len)

    lengths = [1 for i in range(len(strings))]
    sequence = [-1 for i in range(len(strings))]
    
    maxLen = 1
    idx = -1
    for i in range(1,len(strings)):
        for j in range(i):
            if isDistanceOne(strings[i],strings[j]) and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                sequence[i] = j
        
        if maxLen < lengths[i]:
            maxLen= lengths[i]
            idx = i

    result = []
    while idx != -1:
        result.append(strings[idx])
        idx = sequence[idx]
    
    return result


def isDistanceOne(s1,s2):
    if len(s1) - len(s2) != 1:
        return False
    
    i=0
    j=0
    dist = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            dist +=1
            i += 1
        else:
            i +=1
            j +=1

    return dist <=1

strings = [
            "lgoprt",
            "12345678",
            "algoxpert",
            "abcde",
            "123468",
            "lgoxprt",
            "abde",
            "lgopt",
            "1234678",
            "ade",
            "ae",
            "algoxprt",
            "a",
            "1abde",
            "lgpt",
            "123456789",
            "234678",
            "algoexpert",
        ]

strings1 = ["abcdefg", "abdefg", "abdfg", "bdfg", "bfg", "bg", "g"]

strings2 = [
            "abcdefg1",
            "1234c",
            "abdefg2",
            "abdfg",
            "123",
            "122",
            "bgg",
            "g",
            "1a2345",
            "12a345",
        ]
print(longestStringChain(strings2))