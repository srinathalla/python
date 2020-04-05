from collections import defaultdict
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        map = defaultdict(list)

        for i, t in enumerate(transactions):
            tarr = t.split(",")
            map[tarr[0]].append((int(tarr[1]), int(tarr[2]), tarr[3], i))

        res = set()

        for user in map:
            map[user].sort()
            for i in range(len(map[user])):

                for j in range(i+1, len(map[user])):
                    if abs(map[user][i][0] - map[user][j][0]) <= 60 and map[user][i][2] != map[user][i-1][2]:
                        res.add(map[user][i][3])
                        res.add(map[user][j][3])

                if map[user][i][1] > 1000:
                    res.add(map[user][i][3])

        return [transactions[idx] for idx in res]


s = Solution()
print(s.invalidTransactions(["bob,649,842,prague", "alex,175,1127,mexico", "iris,164,119,paris", "lee,991,1570,mexico", "lee,895,1876,taipei", "iris,716,754,moscow", "chalicefy,19,592,singapore", "chalicefy,820,71,newdelhi", "maybe,231,1790,paris", "lee,158,987,mexico", "chalicefy,415,22,montreal", "iris,803,691,milan", "xnova,786,804,guangzhou", "lee,734,1915,prague", "bob,836,1904,dubai", "iris,666,231,chicago", "iris,677,1451,milan", "maybe,860,517,toronto", "iris,344,1452,bangkok", "lee,664,463,frankfurt", "chalicefy,95,1222,montreal", "lee,293,1102,istanbul", "maybe,874,36,hongkong", "maybe,457,1802,montreal", "xnova,535,270,munich", "iris,39,264,istanbul", "chalicefy,548,363,barcelona", "lee,373,184,munich", "xnova,405,957,mexico", "chalicefy,517,266,luxembourg", "iris,25,657,singapore", "bob,688,451,beijing", "bob,263,1258,tokyo", "maybe,140,222,amsterdam", "xnova,852,330,barcelona", "xnova,589,837,budapest", "lee,152,981,mexico", "alex,893,1976,shenzhen", "xnova,560,825,prague", "chalicefy,283,399,zurich", "iris,967,1119,guangzhou", "alex,924,223,milan", "chalicefy,212,1865,chicago", "alex,443,537,taipei", "maybe,390,5,shanghai", "bob,510,1923,madrid", "bob,798,343,hongkong", "iris,643,1703,madrid", "bob,478,928,barcelona",
                             "maybe,75,1980,shanghai", "xnova,293,24,newdelhi", "iris,176,268,milan", "alex,783,81,moscow", "maybe,560,587,milan", "alex,406,776,istanbul", "lee,558,727,paris", "maybe,481,1504,munich", "maybe,685,602,madrid", "iris,678,788,madrid", "xnova,704,274,newdelhi", "chalicefy,36,1984,paris", "iris,749,200,amsterdam", "lee,21,119,taipei", "iris,406,433,bangkok", "bob,777,542,taipei", "maybe,230,1434,barcelona", "iris,420,1818,zurich", "lee,622,194,amsterdam", "maybe,545,608,shanghai", "xnova,201,1375,madrid", "lee,432,520,dubai", "bob,150,1634,singapore", "maybe,467,1178,munich", "iris,45,904,beijing", "maybe,607,1953,tokyo", "bob,901,815,tokyo", "maybe,636,558,milan", "bob,568,1674,toronto", "iris,825,484,madrid", "iris,951,930,dubai", "bob,465,1080,taipei", "bob,337,593,chicago", "chalicefy,16,176,rome", "chalicefy,671,583,singapore", "iris,268,391,chicago", "xnova,836,153,jakarta", "bob,436,530,warsaw", "alex,354,1328,luxembourg", "iris,928,1565,paris", "xnova,627,834,budapest", "xnova,640,513,jakarta", "alex,119,16,toronto", "xnova,443,1687,taipei", "chalicefy,867,1520,montreal", "alex,456,889,newdelhi", "lee,166,3,madrid", "bob,65,1559,zurich", "alex,628,861,moscow", "maybe,668,572,mexico", "bob,402,922,montreal"]))
