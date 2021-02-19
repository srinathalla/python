import collections


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:

        n = len(s)

        arr = [collections.deque() for _ in range(10)]

        for i, x in enumerate(s):
            arr[int(x)].append(i)

        for x in t:
            x = int(x)

            if len(arr[x]) == 0:
                return False

            for j in range(x):
                if len(arr[j]) > 0 and arr[j][0] < arr[x][0]:
                    return False
            arr[x].popleft()
        return True


s = Solution()

st1 = "84532"
t1 = "34852"

print(s.isTransformable(st1, t1))

st2 = "12345"
t2 = "12435"
print(s.isTransformable(st2, t2))
