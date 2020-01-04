# /**
# T.C : O(n*m) as we are computing the result only once
# S.C O(n+m) n is len of one,m len of two
#


def interweavingStrings(one, two, three):
    if len(one) + len(two) != len(three):
        return False

    cache = [[None for j in range(len(two) + 1)]
             for i in range(len(one) + 1)]

    return interweaved(one, two, three, 0, 0, cache)


def interweaved(one, two, three, i, j, cache):

    if cache[i][j] is not None:
        return cache[i][j]

    k = i + j
    if k == len(three):
        return True

    if i < len(one) and three[k] == one[i]:
        cache[i][j] = interweaved(one, two, three, i+1, j, cache)
        if cache[i][j]:
            return True

    if j < len(two) and three[k] == two[j]:
        cache[i][j] = interweaved(one, two, three, i, j + 1, cache)
        if cache[i][j]:
            return True

    cache[i][j] = False
    return False


print(interweavingStrings("abc", "123", "a1b2c3"))
