from collections import Counter


class TwoSum:

    def __init__(self):
        self.m = Counter()

    def add(self, number: int) -> None:
        self.m[number] += 1

    def find(self, value: int) -> bool:
        for k, v in self.m.items():
            other = value - k

            if other == k:
                return v >= 2

            if other in self.m:
                return True

        return False
