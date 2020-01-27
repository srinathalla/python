from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        map = ["", "", "abc", "def", "ghi",
               "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []

        self.recurse(digits, 0, map, "", result)
        return result

    def recurse(self, digits, pos, map, curr, result) -> List[str]:

        if pos == len(digits):
            result.append(curr)
            return

        digit = digits[pos]
        mappedStr = map[int(digit)]

        for mch in mappedStr:
            self.recurse(digits, pos + 1, map, curr + mch, result)


s = Solution()

print(s.letterCombinations("23"))
