from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        map = {}

        for ticket in tickets:
            tos = map.get(ticket[0], [])
            tos.append(ticket[1])
            map[ticket[0]] = tos

        for key in map.keys():
            map[key] = sorted(map.get(key))

        res = []

        def visit(map, s, res):
            if s in map.keys() and len(map.get(s)) > 0:
                adv = map.get(s).pop(0)
                visit(map, adv, res)

            res.append(s)

        visit(map, "JFK", res)
        return res[::-1]


tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
s = Solution()
print(s.findItinerary(tickets))
