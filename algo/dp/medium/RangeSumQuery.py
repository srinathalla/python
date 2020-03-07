class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if len(matrix) > 0:
            self.dp = []
            for i in range(len(matrix)):
                sum = 0
                row = []
                for j in range(len(matrix[0])):
                    sum += matrix[i][j]
                    row.append(sum)
                self.dp.append(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            sum += self.dp[i][col2]
            if col1 > 0:
                sum -= self.dp[i][col1-1]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
