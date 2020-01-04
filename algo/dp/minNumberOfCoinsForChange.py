#
# T.C O(n*m) where m is length of denoms
# S.C O(n)
# 
# #
def minNumberOfCoinsForChange(n, denoms):
    coins = [float('inf') for i in range(n+1)]
    coins[0] = 0

    for i in range(len(denoms)):
        for j in range(1,n+1):
            if j >= denoms[i]:
                coins[j] = min(coins[j], 1 + coins[j-denoms[i]])
    

    return coins[n] if coins[n] != float('inf') else -1


print(minNumberOfCoinsForChange(7, [1, 5, 10]))

    
