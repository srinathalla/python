def getPermutations(array):
    if len(array) <= 1:
        return array
    result = []
    permutate(array,0,result)
    return result


def permutate(array,i,result):
    if i == len(array):
        result.append([*array])
        return
    
    for j in range(i,len(array)):
        swap(array,i,j)
        permutate(array, i + 1,result)
        swap(array,i,j)
        
def swap(array,i,j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

print(getPermutations([1,2,3]))