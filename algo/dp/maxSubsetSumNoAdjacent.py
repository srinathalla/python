##
 # Bottom up approach.
 # 
 # T.C : O(n) as we iterate through array once
 # S.C : O(1) constant space
 # 
 # 
 #
def maxSubsetSumNoAdjacent(array):
   
    if len(array) == 0:
       return 0
    if len(array) == 1:
       return array[0]
    first = array[0]
    second = max(array[1],array[0])

    for i in range(2,len(array)):
        current = max(array[i] + first,second)
        first = second
        second = current
    
    return second

##
 # Top down approach.
 # 
 # T.C : O(n) as each element in cache is computed once.
 # S.C : O(n) as we use an array to cache the result.
 # 
 # 
 #
def maxSubsetSumNoAdjacentRecursive(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    
    maxSum = [float('-inf') for i in range(len(array))]    
    maxSum[0] = array[0]
    maxSum[1] = max(array[0], array[1])

    return recurse(array, len(array) - 1, maxSum)


def recurse(array, i, maxSum):
    if i < 0:
        return 0  

    if maxSum[i] == float('-inf'):
        maxSum[i] = max(
            array[i] + recurse(array, i - 2, maxSum),
            recurse(array, i - 1, maxSum))
    
    return maxSum[i]


print(maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14]))

print(maxSubsetSumNoAdjacentRecursive([7, 10, 12, 7, 9, 14]))

