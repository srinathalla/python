#
# T.C : O(j + d), S.C O(j +d)
# #
def topologicalSort(jobs, deps):
    graph = {}
    visited = {}

    for job in jobs:
        graph[job] = []
        visited[job] = False

    for dep in deps:
        graph[dep[1]].append(dep[0])

    result = []
    dfsStack = set()
    for job in graph.keys():
        if visited[job] is False:
            cycleDetected = dfs(job, graph, visited, result, dfsStack)
            if cycleDetected:
                return []

    return result


def dfs(job, graph, visited, result, dfsStack):

    if job in dfsStack:
        return True
    dfsStack.add(job)

    for adjJob in graph[job]:
        if visited[adjJob] is False:
            cycleDetected = dfs(adjJob, graph, visited, result, dfsStack)
            if cycleDetected:
                return True

    visited[job] = True
    result.append(job)
    dfsStack.remove(job)
    return False


jobs1 = [1, 2, 3, 4]
deps1 = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
print(topologicalSort(jobs1, deps1))

jobs2 = [1, 2, 3, 4, 5, 6, 7, 8]
deps2 = [[3, 1], [8, 1], [8, 7], [5, 7], [
    5, 2], [1, 4], [6, 7], [1, 2], [7, 6]]
print(topologicalSort(jobs2, deps2))
