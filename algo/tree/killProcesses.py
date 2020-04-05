import queue
from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        t = {pa: set() for pa in ppid}

        for i in range(len(pid)):
            pa = ppid[i]
            c = pid[i]
            t[pa].add(c)

        q = queue.Queue(len(pid))
        q.put(kill)

        res = []
        while q.empty() == False:
            v = q.get()
            res.append(v)

            if v in t.keys():
                for av in t[v]:
                    q.put(av)

        return res


pid = [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5

s = Solution()
print(s.killProcess(pid, ppid, kill))
