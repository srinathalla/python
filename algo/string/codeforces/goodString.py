import collections

tc = int(input())


def good(s):

    cnt = collections.Counter(s)
    mc = max(cnt.values())

    for i in range(1, 10):
        for j in range(1, 10):
            count = 0
            for k in range(len(s)-1):
                if s[k] == str(i) and s[k+1] == str(j):
                    count += 2

            mc = max(mc, count)

        mc = max(mc, count)

    return len(s) - mc


for i in range(tc):
    s = input()

    print(good(s))
