#
# T.C : O(n*2^n) we have 2^n subsets created and at each subset creation we iterate through a list of size n for cloning
# S.C : O(n*2^n) we have 2^n subsets created and each subset can store a elements of size n.
#
#
#


def powerset(array):
    subsets = [[]]
    for x in array:
        addElementToExistingSets(subsets, x)

    return subsets


def addElementToExistingSets(sets, x):
    for i in range(len(sets)):
        sets.append(sets[i] + [x])


print(powerset([1, 2, 3]))

print(powerset([1]))
