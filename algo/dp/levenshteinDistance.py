 #
 # T.C : O(2n) + O(m) + O(n*m) => O(nm)
 # @param {*} str1 
 # @param {*} str2 
 #

def levenshteinDistance(str1, str2):
    n = len(str1)
    m = len(str2)
    distances = [[j for j in range(m+1)] for i in range(n+1)]

    for i in range(n+1):
        distances[i][0] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if (str1[i - 1] == str2[j - 1]):
                distances[i][j] = distances[i - 1][j - 1]
            else:
                distances[i][j] = min(distances[i - 1][j - 1], distances[i - 1][j], distances[i][j - 1]) + 1
            
    return distances[n][m]


print(levenshteinDistance('abc', 'yabcx'))
