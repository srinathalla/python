# T.C : O(m + n)
# S.C : O(1)
#
# #


def searchInSortedMatrix(matrix, target):

    r = 0
    c = len(matrix[0]) - 1

    while r < len(matrix) and c >= 0:
        if target > matrix[r][c]:
            r += 1
        elif target < matrix[r][c]:
            c -= 1
        else:
            return [r, c]

    return [-1, -1]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]
print(searchInSortedMatrix(matrix, 43))


print(searchInSortedMatrix(matrix, 103))
