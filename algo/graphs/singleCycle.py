
#
# T.C O(n) + S.C : O(n)
# #


def hasSingleCycleUsingdfs(array):

    visited = [False for x in array]
    return dfs(array, 0, visited, [0])


def dfs(array, i, visited, visitedCount):

    if visited[i]:
        if i == 0 and visitedCount == len(array):
            return True
        return False

    visited[i] = True
    visitedCount[0] += 1

    nextJump = i + array[i]
    nextJump = nextJump % len(array)
    nextJump = nextJump if nextJump >= 0 else nextJump + len(array)

    return dfs(array, nextJump, visited, visitedCount)

# T.C : O(n), S.C O(1)
# #


def hasSingleCycle(array):

    visitedCount = 0
    i = 0
    while visitedCount < len(array):
        if array[i] == 0:
            return False
        visitedCount += 1
        prev = i
        i = getNextJump(array, i)
        array[prev] = 0

    return i == 0


def getNextJump(array, i):
    jump = i + array[i]
    jump = jump % len(array)
    return jump if jump >= 0 else jump + len(array)


print(hasSingleCycle([-1, 2, 2]))

print(hasSingleCycle([1, 1, 1, 1, 2]))

print(hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 909, -26]))
