#
# T.C : O(nc) where n is the no of items and c is the capacity
# S.C : O(nc) where n is the no of items and c is the capacity
# #


def knapsackProblem(items, capacity):
    table = [[0 for j in range(capacity + 1)] for i in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            if j >= items[i-1][1]:
                table[i][j] = max(table[i-1][j], table[i-1]
                                  [j-items[i-1][1]] + items[i-1][0])
            else:
                table[i][j] = table[i-1][j]

    result = []

    i = len(items)
    j = capacity

    while i > 0 and j > 0:
        if table[i][j] == table[i-1][j]:
            i -= 1
        else:
            result.append(i-1)
            j -= items[i-1][1]
            i -= 1

    return [table[len(items)][capacity], list(reversed(result))]


print(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))
