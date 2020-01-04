#
# T.C : O(n*k) S.C : O(n*k)
# #


def maxProfitWithKTransactions(prices, k):

    if len(prices) <= 1:
        return 0

    table = [[0 for p in prices] for i in range(k+1)]

    for t in range(1, k+1):
        profit = -prices[0]
        for i in range(1, len(prices)):
            table[t][i] = max(table[t][i-1], prices[i] + profit)
            profit = max(profit, table[t-1][i-1] - prices[i])

    return table[t][len(prices)-1]


print(maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2))
