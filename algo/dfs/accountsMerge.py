from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        if len(accounts) < 2:
            return accounts

        g = {}
        name = {}

        for a in accounts:
            for i in range(1, len(a)):
                if a[i] not in g.keys():
                    g[a[i]] = []

                name[a[i]] = a[0]

                if i > 1:
                    g[a[i]].append(a[i-1])
                    g[a[i-1]].append(a[i])

        def dfs(g, mail, visited, group):
            visited.add(mail)
            group.append(mail)

            for am in g[mail]:
                if am not in visited:
                    dfs(g, am, visited, group)

        visited = set()
        res = []

        for mail in name.keys():
            user = name[mail]
            group = []
            if mail not in visited:
                dfs(g, mail, visited, group)
                group.sort()
                group.insert(0, user)
                res.append(group)
        return res


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], [
    "John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]


s = Solution()
accounts = s.accountsMerge(accounts)
print(accounts)
