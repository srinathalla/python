
# T.C : O(n^2) + O(nlogn) => O(n^2)
# S.C : O(n)
#
# @param {} disks
#


def diskStacking(disks):

    disks.sort(key=lambda x: x[2])
    heights = [x[2] for x in disks]
    sequence = [-1 for h in heights]
    maxIdx = 0

    for i in range(len(disks)):
        for j in range(0, i):
            if isValidStack(disks[j], disks[i]) and heights[i] <= heights[j] + disks[i][2]:
                heights[i] = heights[j] + disks[i][2]
                sequence[i] = j

        if heights[maxIdx] <= heights[i]:
            maxIdx = i

    result = []
    idx = maxIdx
    while idx != -1:
        result.append(disks[idx])
        idx = sequence[idx]

    return list(reversed(result))


def isValidStack(disk1, disk2):
    return disk1[0] < disk2[0] and disk1[1] < disk2[1] and disk1[2] < disk2[2]


print(diskStacking([[2, 1, 2], [3, 2, 3], [
      2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]))
