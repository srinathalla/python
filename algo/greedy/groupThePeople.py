from typing import List


class Solution:
    def groupThePeople(self, g: List[int]) -> List[List[int]]:
        c = [[i, v] for i, v in enumerate(g)]
        c.sort(key=lambda x: x[1])

        res = []
        while len(c) > 0:
            item = c.pop(0)
            group = []
            group.append(item[0])

            while len(group) < item[1]:
                group.append(c.pop(0)[0])

            res.append(group)
        return res


g = [3, 3, 3, 3, 3, 1, 3]
s = Solution()
print(s.groupThePeople(g))
