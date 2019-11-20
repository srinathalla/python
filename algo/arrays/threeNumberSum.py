def threeNumberSum(array, targetSum):
    array.sort()
    result = []

    for i in range(len(array)):
        itemsSet = set()
        newTargetSum = targetSum - array[i]
        for j in range(i+1, len(array)):
            if newTargetSum - array[j] in itemsSet:
                result.append([array[i], newTargetSum - array[j], array[j]])
            itemsSet.add(array[j])

    result.sort(key=lambda item: (item[0], item[1]))
    return result


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
