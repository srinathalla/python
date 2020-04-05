from enum import Enum
from typing import List


class format(Enum):
    Year = 1
    Month = 2
    Day = 3
    Hour = 4
    Minute = 5
    Second = 6


class LogSystem:

    def __init__(self):
        self.logs = {}

    def put(self, id: int, timestamp: str) -> None:
        self.logs[id] = list(map(int, timestamp.split(":")))

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        start = list(map(int, s.split(":")))
        end = list(map(int, e.split(":")))

        def inRange(log, i):
            sl = False
            eb = False
            for k in range(i):
                if start[k] == log[k]:
                    continue
                elif start[k] < log[k]:
                    sl = True
                    break
                else:
                    return False

            for k in range(i):
                if log[k] == end[k]:
                    continue
                elif log[k] < end[k]:
                    eb = True
                    break
                else:
                    return False

            return True

        frmt = None
        for f in format:
            if f.name == gra:
                frmt = f
                break

        res = []
        for id, timestamp in self.logs.items():
            if inRange(timestamp, frmt.value):
                res.append(id)

        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)

log = LogSystem()
log.put(1, "2017:01:01:23:59:59")
log.put(22, "2017:01:02:23:59:59")
print(log.retrieve("2017:01:01:23:59:58", "2017:01:02:23:59:58", "Second"))
