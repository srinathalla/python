def moveElementToEnd(array, toMove):
    i = 0
    j = 0
    while j < len(array):
        if array[j] != toMove:
            swap(array, i, j)
            i += 1
        j += 1
    return array


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
