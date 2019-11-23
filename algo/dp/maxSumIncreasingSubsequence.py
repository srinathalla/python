def maxSumIncreasingSubsequence(array):
    
    if len(array) == 1:
        return [array[0],[array[0]]]
    
    maxIdx = 0
    sequence = [i for i in range(len(array))]
    maxSumArray = [x for x in array]


    for i in range(1,len(array)):
        for j in range(0,i):
            if array[i] > array[j] and maxSumArray[i] < maxSumArray[j] + array[i]:
                maxSumArray[i] = maxSumArray[j] + array[i]
                sequence[i] = j 
        if maxSumArray[maxIdx] < maxSumArray[i]:
            maxIdx= i
    
    i = maxIdx
    result = []
    while i >= 0:
        result.insert(0,array[i])
        i = sequence[i]  if i != sequence[i] else -1
    
    return [maxSumArray[maxIdx], result]


print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))

print(maxSumIncreasingSubsequence([-1, 1]))

