#
# T.C O(m*n) m no of rows,
#            n  no of columns
# S.C O(1)
# #


def riverSizes(matrix):

    result = []
    count = [0]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                dfs(matrix, i, j, count)
                result.append(count[0])
                count[0] = 0

    return result


def dfs(matrix, r, c, count):
    if r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[0]) and matrix[r][c] == 1:
        count[0] += 1
        matrix[r][c] = 0
        dfs(matrix, r, c + 1, count)
        dfs(matrix, r, c - 1, count)
        dfs(matrix, r + 1, c, count)
        dfs(matrix, r - 1, c, count)


testInput = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
]

print(riverSizes(testInput))
