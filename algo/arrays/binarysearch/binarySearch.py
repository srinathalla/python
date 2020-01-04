def binarySearch(array, target):

    l = 0
    r = len(array) - 1

    while l < r:
        m = (l+r)//2

        if array[m] == target:
            return m
        elif array[m] < target:
            l = m + 1
        else:
            r = m - 1

    return l if array[l] == target else -1


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
