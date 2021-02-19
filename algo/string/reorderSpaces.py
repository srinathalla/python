class Solution:
    def reorderSpaces(self, text: str) -> str:

        sc = 0
        words = []
        word = ""
        for a in text:
            if a == ' ':
                sc += 1
                if len(word.strip()) > 0:
                    words.append(word.strip())
                    word = ""
            else:
                word += a

        if len(word.strip()) > 0:
            words.append(word.strip())

        if len(words) == 1:
            return words.pop() + ''.join([" "]*sc)

        gap = sc//(len(words) - 1)
        suffix = sc % (len(words) - 1)

        res = ""
        for w in words:
            res += w
            res += ''.join([" "]*sc)

        res = res.strip()

        return res + ''.join([" "]*suffix)


text = "  this   is  a sentence "

s = Solution()
print(s.reorderSpaces(text))
