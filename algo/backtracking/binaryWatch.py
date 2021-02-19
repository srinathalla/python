from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    res.append('%d:%02d' % (h, m))

        return res


s = Solution()
print(s.readBinaryWatch(1))
