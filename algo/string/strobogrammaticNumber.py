
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        map = {}
        map['0'] = '0'
        map['1'] = '1'
        map['6'] = '9'
        map['8'] = '8'
        map['9'] = '6'

        i, j = 0, len(num)-1

        while i <= j and num[i] in map and num[j] == map[num[i]]:
            i += 1
            j -= 1

        return i > j


s = Solution()
print(s.isStrobogrammatic("69"))
print(s.isStrobogrammatic("66"))
