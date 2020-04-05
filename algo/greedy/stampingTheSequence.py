from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:

        tarr = [a for a in target]
        star = 0
        visited = [False]*len(target)
        res = []

        def canReplace(str, p, stamp):
            for i in range(len(stamp)):
                if str[p + i] != '*' and str[p + i] != stamp[i]:
                    return False
            return True

        def doReplace(tarr, p, len):
            c = 0
            for i in range(len):
                if tarr[p+i] != '*':
                    tarr[p+i] = '*'
                    c += 1
            return c

        while star < len(target):
            replaced = False

            for i in range(len(target) - len(stamp) + 1):
                if visited[i] == False and canReplace(tarr, i, stamp):
                    star += doReplace(tarr, i, len(stamp))
                    replaced = True
                    visited[i] = True
                    res.append(i)

                if star == len(target):
                    break

            if replaced == False:
                return []

        res = res[::-1]

        return res


stamp = "abca"
target = "aabcaca"
s = Solution()
print(s.movesToStamp(stamp, target))
