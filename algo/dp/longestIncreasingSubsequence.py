#
#  T.C : O(n^2)
#  S.C : O(n)
#
def longestIncreasingSubsequence(array):

    lengths = [1 for i in range(len(array))]
    sequences = [i for i in range(len(array))]
    
    maxIdx = 0
    for i in range(1,len(array)): 
        for j in range(0,i):
            if (array[i] > array[j] and lengths[i] < lengths[j] + 1):
                lengths[i] = lengths[j] + 1
                sequences[i] = j
                if (lengths[maxIdx] < lengths[i]):
                    maxIdx = i
                
    result = []
    i = maxIdx
    while (i >= 0):
        result.insert(0,array[i])
        i = sequences[i] if i != sequences[i] else -1
    
    return result


print(longestIncreasingSubsequence([
    5,
    7,
    -24,
    12,
    10,
    2,
    3,
    12,
    5,
    6,
    35,
]))
