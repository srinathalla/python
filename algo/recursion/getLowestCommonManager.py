#
# T.C O (n + d) where d is depth of tree
#  S.C : O(2d)


def getLowestCommonManagerWithStoringPaths(topManager, reportOne, reportTwo):
    paths = [None, None]
    search(topManager, reportOne, reportTwo, [], paths)

    i = 0
    j = 0
    prev = None
    while i < len(paths[0]) and j < len(paths[1]) and paths[0][i] == paths[1][j]:
        prev = paths[0][i]
        i += 1
        j += 1

    return prev


def search(employee, reportOne, reportTwo, path, paths):
    if paths[0] is not None and paths[1] is not None:
        return True

    path.append(employee)
    if employee == reportOne:
        paths[0] = list(path)

    if employee == reportTwo:
        paths[1] = list(path)

    for dirReport in employee.directReports:
        bothFound = search(dirReport, reportOne, reportTwo, path, paths)
        if bothFound:
            return True

    path.pop(len(path)-1)

    return False

#
# T.C : O(n) S.C :O(d) where d is the depth of the tree
# #


def getLowestCommonManager(topManager, reportOne, reportTwo):
    return recurse(topManager, reportOne, reportTwo).commonManager


def recurse(manager, reportOne, reportTwo):
    importantReports = 0
    for report in manager.directReports:
        orgInfo = recurse(report, reportOne, reportTwo)
        if orgInfo.commonManager is not None:
            return orgInfo
        importantReports += orgInfo.importantReports

    if manager == reportOne or manager == reportTwo:
        importantReports += 1

    commonManager = manager if importantReports == 2 else None

    return OrgInfo(commonManager, importantReports)


class OrgInfo:
    def __init__(self, commonManager, importantReports):
        self.commonManager = commonManager
        self.importantReports = importantReports


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

    def addDirectReports(self, directReports):
        for directReport in directReports:
            self.directReports.append(directReport)


orgCharts = {}
ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for letter in ALPHABET:
    orgCharts[letter] = OrgChart(letter)
orgCharts["A"].addDirectReports(
    [orgCharts["B"], orgCharts["C"], orgCharts["D"], orgCharts["E"], orgCharts["F"]]
)
orgCharts["B"].addDirectReports(
    [orgCharts["G"], orgCharts["H"], orgCharts["I"]])
orgCharts["C"].addDirectReports([orgCharts["J"]])
orgCharts["D"].addDirectReports([orgCharts["K"], orgCharts["L"]])
orgCharts["F"].addDirectReports([orgCharts["M"], orgCharts["N"]])
orgCharts["H"].addDirectReports(
    [orgCharts["O"], orgCharts["P"], orgCharts["Q"], orgCharts["R"]]
)
orgCharts["K"].addDirectReports([orgCharts["S"]])
orgCharts["P"].addDirectReports([orgCharts["T"], orgCharts["U"]])
orgCharts["R"].addDirectReports([orgCharts["V"]])
orgCharts["V"].addDirectReports(
    [orgCharts["W"], orgCharts["X"], orgCharts["Y"]])
orgCharts["X"].addDirectReports([orgCharts["Z"]])


print(getLowestCommonManager(
    orgCharts["A"], orgCharts["G"], orgCharts["M"]
).name)
