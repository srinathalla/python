import collections


def count(s):
    cnt = collections.Counter(s)

    len = 0
    for i in range(len(s)):
        cnt = collections.Counter()
        for j in range(i, len(s)):
            cnt[s[j]] += 1

            if cnt.get('a', 0) == 1 + cnt.get('b', 0):
                len = max(len, s[i:j+1])

        cnt[s[i]] -= 1

    return len
