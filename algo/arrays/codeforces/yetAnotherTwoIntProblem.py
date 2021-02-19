# You are given two integers 𝑎 and 𝑏.
# In one move, you can choose some integer 𝑘 from 1 to 10 and add it to 𝑎 or subtract it from 𝑎. In other words, you choose an integer 𝑘∈[1;10] and perform 𝑎:=𝑎+𝑘 or 𝑎:=𝑎−𝑘. You may use different values of 𝑘 in different moves.
# Your task is to find the minimum number of moves required to obtain 𝑏 from 𝑎.
# You have to answer 𝑡 independent test cases.

tc = int(input())


def minMoves(a, b):
    d = abs(a-b)
    return d//10 + (1 if d % 10 > 0 else 0)


for i in range(tc):
    s = input()
    a, b = s.split()
    print(minMoves(int(a), int(b)))
