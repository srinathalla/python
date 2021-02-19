tc = int(input())


def B(A, K):
    tot = 0
    tot += max(0, K-A)
    A += tot

    if A & 1 == 1:
        if K & 1 == 0:
            tot += 1
    else:
        if K & 1 == 1:
            tot += 1

    return tot


for i in range(tc):
    tc = input()
    A, K = tc.split()

    print(B(int(A), int(K)))
