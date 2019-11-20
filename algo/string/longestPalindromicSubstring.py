def longestPalindromicSubstring(string):
  
    maxLongest= [0,1]
    for i in range(len(string)):
        odd = expand(string, i,i)
        even = expand(string, i,i+1)

        longest = max(odd, even, key= lambda x: x[1] - x[0])
        maxLongest = max(maxLongest, longest, key= lambda x: x[1] - x[0])

    return string[maxLongest[0]:maxLongest[1]]


def expand(string,i,j):
   
    start = i
    end = j
    while start >=0 and end < len(string) and string[start] == string[end]:
        start -=1
        end +=1
    
    return [start + 1, end] if start < i else [-1,-1]

print(longestPalindromicSubstring("abaxyzzyxf"))