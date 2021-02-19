from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []

        def dfs(i, st, k, path):
            if len(st) == 0 or k == 4:
                if len(st) == 0 and k == 4:
                    res.append(path[1:])

                return

            for j in range(1, min(4, len(st)+1)):

                if j > 1 and st[i] == '0':
                    break

                ss = st[i:i+j]
                if int(ss) > 255:
                    break

                dfs(0, st[i+j:], k+1, path + '.' + ss)

        dfs(0, s, 0, '')
        return res


s = Solution()
print(s.restoreIpAddresses("25525511135"))
