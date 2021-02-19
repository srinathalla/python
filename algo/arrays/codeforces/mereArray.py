tc = int(input())

Y = "YES"
N = "NO"


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def possible(arr):
    if len(arr) == 1:
        return Y

    mi = min(arr)

    s = []
    n = len(arr)
    for i in range(n):
        if gcd(arr[i], mi) == mi:
            s.append(arr[i])
            arr[i] = -1

    s.sort()
    j = 0

    for i in range(n):
        if arr[i] == -1:
            arr[i] = s[j]
            j += 1

    return all(arr[i] >= arr[i-1] for i in range(1, n))


for i in range(tc):
    n = input()
    arr = input()
    arr = arr.split()
    arr = list(map(int, arr))

    print(Y if possible(arr) else N)
