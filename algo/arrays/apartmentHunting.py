
def apartmentHunting(blocks, reqs):
    closestDistances = list(
        map(lambda req: getClosestDistances(blocks, req), reqs))
    minIdx = -1
    minVal = float('inf')
    i = 0
    while i < len(blocks):
        maxDistance = float('-inf')
        j = 0
        while j < len(reqs):
            maxDistance = max(maxDistance, closestDistances[j][i])
            j += 1
        if(maxDistance < minVal):
            minVal = maxDistance
            minIdx = i
        i += 1

    return minIdx


def getClosestDistances(blocks, req):
    closestDistances = [0 for block in blocks]
    closestIdx = float('inf')
    j = 0
    while (j < len(blocks)):
        if blocks[j][req]:
            closestIdx = j
        closestDistances[j] = abs(j - closestIdx)
        j += 1

    j = len(blocks) - 1
    while j >= 0:
        if (blocks[j][req]):
            closestIdx = j
        closestDistances[j] = min(closestDistances[j], abs(j - closestIdx))
        j -= 1
    return closestDistances


blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]
reqs = ["gym", "school", "store"]
print(apartmentHunting(blocks, reqs))
