from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:

        fullSentence = ""
        for word in sentence:
            fullSentence += word + " "

        l = len(fullSentence)

        dp = [0 for _ in range(l)]

        for i in range(1, l):
            dp[i] = 1 if fullSentence[i] == " " else dp[i-1] - 1

        count = 0
        for i in range(rows):
            count += cols
            count += dp[count % l]

        return count//l


rows = 2
cols = 8
sentence = ["hello", "world"]
s = Solution()
print(s.wordsTyping(sentence, rows, cols))
