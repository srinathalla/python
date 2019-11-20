

"""
  T.C O(nlogn) + O(mlogm)
  @param {*} arrayOne 
  @param {*} arrayTwo 
"""


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0

    minDiff = float('inf')
    num1 = -1
    num2 = -1

    while (i < len(arrayOne) and j < len(arrayTwo)):
        diff = abs(arrayOne[i] - arrayTwo[j])
        if (arrayOne[i] < arrayTwo[j]):
            if (minDiff > diff):
                minDiff = diff
                num1 = arrayOne[i]
                num2 = arrayTwo[j]
            i += 1
        elif (arrayOne[i] > arrayTwo[j]):
            if (minDiff > diff):
                minDiff = diff
                num1 = arrayOne[i]
                num2 = arrayTwo[j]
            j += 1
        else:
            return [arrayOne[i], arrayTwo[j]]
    return [num1, num2]


print(smallestDifference([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]))
