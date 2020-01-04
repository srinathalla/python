def kadanesAlgorithm(array):

    globalMax = array[0]
    maxVal = 0
    for no in array:
        maxVal = max(no, no + maxVal)
        globalMax = max(globalMax, maxVal)

    return globalMax


print(kadanesAlgorithm([1, 2, 3, 4, 5, 6, -20, 7, 8, 9, 10]))
