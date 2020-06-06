class Solution:
    def originalDigits(self, s: str) -> str:

        cnt = [0]*10
        for c in s:
            if c == 'z':
                cnt[0] += 1
            elif c == 'w':
                cnt[2] += 1
            elif c == 'u':
                cnt[4] += 1
            elif c == 'x':
                cnt[6] += 1
            elif c == 'g':
                cnt[8] += 1
            elif c == 's':
                cnt[7] += 1  # 7-6
            elif c == 'f':
                cnt[5] += 1  # 5-4
            elif c == 'h':
                cnt[3] += 1 // 3-8
            elif c == 'o':
                cnt[1] += 1  # 1-0-2-4
            elif c == 'i':
                cnt[9] += 1  # 9-8-5-6

        print(cnt)
        cnt[7] -= cnt[6]
        cnt[5] -= cnt[4]
        cnt[3] -= cnt[8]
        cnt[1] = cnt[1] - cnt[0] - cnt[2] - cnt[4]
        cnt[9] = cnt[9] - cnt[8] - cnt[5] - cnt[6]

        print(cnt)
        res = []
        for i in range(10):
            res.extend([i] * cnt[i])

        return ''.join(map(str, res))


s = Solution()
print(s.originalDigits("owoztneoer"))
