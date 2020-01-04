#
# T.C : O(logn) S.C : O(1)
# #


def shiftedBinarySearch(array, target):
    l = 0
    r = len(array)-1
    while l < r:
        m = (l + r)//2
        if array[m] == target:
            return m
        elif array[m] < array[r]:
            if array[m] < target and target <= array[r]:
                l = m + 1
            else:
                r = m - 1
        elif array[m] > array[r]:
            if array[l] <= target and target < array[m]:
                r = m - 1
            else:
                l = m + 1

    return l if array[l] == target else -1


print(shiftedBinarySearch([5, 23, 111, 1], 111))

print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33))
