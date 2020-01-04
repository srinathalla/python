#
# 
# T.C : n^n exponential.
# #
def numberOfWaysToMakeChangeWithRecursion(n, denoms):
    denoms.sort()
    return recurse(n,denoms,0,0)

def recurse(n,denoms,sum,i):
    if sum == n:
        return 1
    if sum > n or i >= len(denoms):
        return 0

    ways = 0
    if sum + denoms[i] <= n:
        ways = recurse(n,denoms, sum + denoms[i],i) + recurse(n,denoms,sum,i+1)

    return ways

#
# T.C : O(n*m) where m is length of denoms
#                    n is the sum
# S.C : O(n)
# 
def numberOfWaysToMakeChange(n,denoms):
    ways = [0 for j in range(n+1)]
    ways[0] = 1

    for i in range(1,len(denoms) + 1):
        for j in range(1,n+1):
            if denoms[i-1] <= j:
                ways[j] += ways[j-denoms[i-1]]
    
    return ways[n]


print(numberOfWaysToMakeChangeWithRecursion(10, [1, 5, 10, 25]))
print(numberOfWaysToMakeChange(10, [1, 5, 10, 25]))

    
