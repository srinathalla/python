"""
T.C : O(n)
Single pass solution.
"""


def twoNumberSum(array, targetSum):
    itemsSet = set()

    for no in array:
        if targetSum - no in itemsSet:
            return [no, targetSum-no] if no < targetSum - no else [targetSum - no, no]
        itemsSet.add(no)

    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
