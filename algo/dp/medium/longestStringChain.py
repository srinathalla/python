from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words = list(map(sorted, words))

        words.sort(key=lambda x: len(x))

        seq = [1] * n

        def isPredecessor(s1, s2):
            if len(s1) != len(s2) - 1:
                return False

            i = 0
            j = 0
            cnt = 0
            while i < len(s1) and j < len(s2):
                if s1[i] != s2[j]:
                    cnt += 1
                    j += 1
                else:
                    i += 1
                    j += 1

            return cnt <= 1

        res = 1
        for i in range(1, n):
            for j in range(i):
                if isPredecessor(words[j], words[i]) and seq[i] < seq[j] + 1:
                    seq[i] = seq[j] + 1
            res = max(res, seq[i])
        return res


s = Solution()
print(
    s.longestStrChain(["czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh",
                       "zczpzfvdhx"]))
