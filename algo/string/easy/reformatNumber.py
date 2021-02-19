class Solution:
    def reformatNumber(self, s: str) -> str:

        res = []

        s = s.replace('-', '').replace(' ', '')
        while len(s) > 4:
            res.append(s[:3])
            s = s[3:]

        if len(s) == 4:
            res.append(s[:2])
            res.append(s[2:])
        else:
            res.append(s)

        return '-'.join(res)
