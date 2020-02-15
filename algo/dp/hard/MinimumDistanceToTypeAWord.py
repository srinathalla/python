import string


class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(c1, c2):
            if c1 is None:
                return 0
            x1, y1 = keyboard[c1]
            x2, y2 = keyboard[c2]
            return abs(x1-x2) + abs(y1-y2)

        def helper(i, f1, f2):
            print("i :" + str(i) + " f1: " + str(f1) + " f2: " + str(f2))
            if i == len(word):
                return 0
            if (i, f1, f2) in memo:
                return memo[(i, f1, f2)]
            choice1 = dist(f1, word[i]) + helper(i + 1, word[i], f2)
            choice2 = dist(f2, word[i]) + helper(i + 1, f1, word[i])
            memo[(i, f1, f2)] = min(choice1, choice2)
            # print(memo)
            return memo[(i, f1, f2)]

        keyboard = {}
        for i, c in enumerate(string.ascii_uppercase):
            keyboard[c] = (i//6, i % 6)

        memo = {}
        return helper(0, None, None)


s = Solution()
print(s.minimumDistance("CAKE"))
