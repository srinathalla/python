class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0

        map = [0 for i in range(10)]

        for i in range(len(secret)):
            map[ord(secret[i]) - ord('0')] += 1

        for i in range(len(secret)):
            ch = ord(secret[i]) - ord('0')
            if ch == ord(guess[i]) - ord('0'):
                a += 1
                map[ch] -= 1

        for i in range(len(secret)):
            ch1 = ord(secret[i]) - ord('0')
            ch2 = ord(guess[i]) - ord('0')
            if ch1 != ch2 and map[ch2] > 0:
                b += 1
                map[ch2] -= 1

        return f'{a}A{b}B'


s = Solution()
secret = "1807"
guess = "7810"
print(s.getHint(secret, guess))
print(s.getHint("1123", "0111"))
