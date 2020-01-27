from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {}
        visited = {}
        order = []
        dfsStack = set()

        for i in range(numCourses):
            graph[i] = []
            visited[i] = False

        for edge in prerequisites:
            graph[edge[0]].append(edge[1])

        for i in range(numCourses):
            if visited[i] == False:
                hasCycle = self.topologicalOrder(
                    graph, visited, i, order, dfsStack)
                if hasCycle:
                    return []

        return order

    def topologicalOrder(self, graph, visited, v, order, dfsStack):
        if visited[v]:
            return

        if v in dfsStack:
            return True
        dfsStack.add(v)
        adjvs = graph[v]

        for adjv in adjvs:
            hasCycle = self.topologicalOrder(
                graph, visited, adjv, order, dfsStack)
            if hasCycle == True:
                return True

        visited[v] = True
        dfsStack.discard(v)
        order.append(v)

        return False


s = Solution()
print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(s.findOrder(2, [[1, 0], [0, 1]]))
