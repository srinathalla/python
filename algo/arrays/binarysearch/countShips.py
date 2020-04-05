class Sea(object):
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if sea.hasShips(topRight, bottomLeft):
            return 0

        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1

        midx = topRight.x + bottomLeft.x >> 1
        midy = topRight.y + bottomLeft.y >> 1

        return self.countShips(sea, Point(midx, midy), bottomLeft) + self.countShips(sea, topRight, Point(midx + 1, midy + 1)) + self.countShips(sea, Point(topRight.x, midy), Point(midx + 1, bottomLeft.y)) + self.countShips(sea, Point(midx, topRight.y), Point(bottomLeft.x, midy + 1))


s = Solution()
s.countShips
