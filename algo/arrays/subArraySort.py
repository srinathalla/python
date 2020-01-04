#
#  T.C : O(2n) => O(n) S.C : O(1)
#


def subarraySort(array):
    minOutOfOrder = float('inf')
    maxOutOfOrder = float('-inf')

    for i in range(len(array)):
        if isOutOfOrder(i, array[i], array):
            minOutOfOrder = min(minOutOfOrder, array[i])
            maxOutOfOrder = max(maxOutOfOrder, array[i])

    if minOutOfOrder == float('inf'):
        return [-1, -1]

    leftSubIdx = 0
    while minOutOfOrder >= array[leftSubIdx]:
        leftSubIdx += 1

    rightSubIdx = len(array)-1
    while maxOutOfOrder <= array[rightSubIdx]:
        rightSubIdx -= 1

    return [leftSubIdx, rightSubIdx]


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i+1]
    if i == len(array) - 1:
        return num < array[i-1]
    return num < array[i-1] or num > array[i+1]


print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
