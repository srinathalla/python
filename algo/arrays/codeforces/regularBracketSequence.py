

def RBS(seq):

    n = len(seq)
    if n & 1 == 1:
        return "NO"

    if seq[0] == ')' or seq[-1] == '(':
        return "NO"

    return "YES"


tc = int(input())

for i in range(tc):
    seq = input()
    print(RBS(seq))
