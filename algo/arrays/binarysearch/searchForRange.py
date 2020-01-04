#
# T.C : O(2nlogn) =>  O(nlogn)
# #


def searchForRange(array, target):
    l = searchForFirst(array, target)
    if l == -1:
        return [-1, -1]
    r = searchForLast(array, target)

    return [l, r]


def searchForFirst(array, target):

    l = 0
    r = len(array) - 1
    while l < r:
        m = (l + r)//2
        if array[m] > target:
            r = m - 1
        elif array[m] < target:
            l = m + 1
        else:
            if m == 0 or array[m-1] != target:
                return m
            else:
                r = m - 1

    return l if array[l] == target else -1


def searchForLast(array, target):
    l = 0
    r = len(array) - 1
    while l < r:
        m = (l + r)//2
        if array[m] > target:
            r = m - 1
        elif array[m] < target:
            l = m + 1
        else:
            if m == len(array)-1 or array[m+1] != target:
                return m
            else:
                l = m + 1

    return l if array[l] == target else -1


# print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], -1))

print(searchForRange([5, 7, 7, 8, 8, 10], 7))
