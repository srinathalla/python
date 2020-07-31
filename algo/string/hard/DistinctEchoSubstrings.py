class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        res = set()

        for i in range(len(text)):
            for j in range(2, len(text) - i + 1, 2):
                mid = i + j//2

                if text[i:mid] == text[mid:i + j]:
                    res.add(text[i:mid])

        print(res)
        return len(res)


s = Solution()
print(s.distinctEchoSubstrings("aaaaaaaaaa"))
