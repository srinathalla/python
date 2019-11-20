def largestRange(array):
    itemsSet = set()
    for x in array:
        itemsSet.add(x)

    maxRange = 0
    start = -1
    for x in array:
        if (not(x - 1 in itemsSet)):
            count = 0
            y = x
            while (y in itemsSet):
                count += 1
                y += 1
            if count > maxRange:
                maxRange = count
                start = x

    result = [start, start + maxRange - 1]
    return result


print(largestRange([1]))
print(largestRange([4, 2, 1, 3, 6]))
