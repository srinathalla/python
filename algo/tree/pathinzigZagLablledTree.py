from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = 0
        while 1 << level <= label:
            level += 1

        res = [0]*level
        while label >= 1:
            res[level-1] = label
            label = (1 << level) - 1 - label + (1 << (level - 1))
            label = label//2
            level -= 1
        return res


s = Solution()
print(s.pathInZigZagTree(14))
