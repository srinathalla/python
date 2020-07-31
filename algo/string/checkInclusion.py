from typing import List
import heapq
import collections
from collections import defaultdict


class TreeAncestor:
    step = 15

    def __init__(self, n: int, A: List[int]):
        A = dict(enumerate(A))
        jump = [A]
        for s in range(self.step):
            B = {}
            for i in A:
                if A[i] in A:
                    B[i] = A[A[i]]
            jump.append(B)
            A = B
        self.jump = jump

    def getKthAncestor(self, x: int, k: int) -> int:
        step = self.step
        while k > 0 and x > -1:
            if k >= 1 << step:
                x = self.jump[step].get(x, -1)
                k -= 1 << step
            else:
                step -= 1
        return x


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

arr = [4, 3, 1, 1, 3, 3, 2]
k = 3


tree = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
#print(tree.getKthAncestor(3, 1))
#print(tree.getKthAncestor(5, 2))
print(tree.getKthAncestor(6, 3))
