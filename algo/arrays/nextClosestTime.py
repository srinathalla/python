class Solution:
    def nextClosestTime(self, time: str) -> str:
        def getTime(no):
            return f'0{no}' if no < 10 else f'{no}'

        charset = set()
        for ch in time:
            if ch != ':':
                charset.add(ch)

        minutes = int(time[:2])*60 + int(time[3:])

        while True:
            minutes += 1
            minutes = minutes % (24*60)

            hrs = minutes//60
            mins = minutes % 60

            allPresent = True
            time = getTime(hrs) + getTime(mins)

            for ch in time:
                if ch not in charset:
                    allPresent = False
                    break

            if allPresent:
                return getTime(hrs) + ':' + getTime(mins)


s = Solution()
# print(s.nextClosestTime("19:34"))
print(s.nextClosestTime("23:59"))
