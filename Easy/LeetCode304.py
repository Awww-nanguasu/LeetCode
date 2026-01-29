class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        Row = len(matrix)
        Col = len(matrix[0])
        if Row == 0 or Col == 0:
            return
        self.PreSum = [[0]*(Col+1) for _ in range(Row+1)] 
        for i in range(1, Row+1):
            for j in range(1, Col+1):
                self.PreSum[i][j] = (self.PreSum[i - 1][j] + self.PreSum[i][j - 1] +
                                     matrix[i - 1][j - 1] - self.PreSum[i - 1][j - 1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.PreSum[row2+1][col2+1] - self.PreSum[row2+1][col1] - self.PreSum[row1][col2+1] + self.PreSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)