from typing import List


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.n = len(v)
        self.r = 0
        self.c = 0
        self.v = v

    def next(self) -> int:
        if self.hasNext():
            val = self.v[self.r][self.c]
            self.c += 1

            if self.c == len(self.v[self.r]):
                self.r += 1
                self.c = 0

            return val

        return -1

    def hasNext(self) -> bool:

        return self.r < self.n and self.c < len(self.v[self.r])


vector2d = Vector2D([[1, 2], [3], [4]])
print(vector2d.next())
print(vector2d.next())
print(vector2d.hasNext())
print(vector2d.hasNext())
print(vector2d.next())
print(vector2d.hasNext())
print(vector2d.next())


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
