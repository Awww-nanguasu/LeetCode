from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        cnt = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, c in enumerate(row):
                cnt[i + 1][j + 1] = cnt[i + 1][j] + cnt[i][j + 1] - cnt[i][j] + c
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            row1 = max(0, i - k)
            row2 = min(m - 1, i + k)
            for j in range(n):
                col1 = max(0, j - k)
                col2 = min(n - 1, j + k)
                ans[i][j] = cnt[row2 + 1][col2 + 1] - cnt[row2 + 1][col1] - cnt[row1][col2 + 1] + cnt[row1][col1]
        return ans
    
class Solution:
    def PreSumFunction(self, mat: List[List[int]], k: int):
        self.row = len(mat)
        self.col = len(mat[0])

        PreSum = [[0]*(self.row+k) for _ in range(self.col+k)]

        for i in range(k, self.row+k):
            for j in range(k, self.col+k):
                PreSum[i][j] = PreSum[i][j-1] + PreSum[i-1][j] + mat[i-k][j-k] - PreSum[i-1][j-1] 
        return PreSum

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        PreSum = [[0]*(row+k) for _ in range(col+k)]

        for i in range(2*k, row+2*k):
            for j in range(2*k, col+2*k):
                PreSum[i][j] = PreSum[i][j-1] + PreSum[i-1][j] + mat[i-k][j-k] - PreSum[i-1][j-1]
                Answer[i-k][j-k] = PreSum[i,j] - PreSum[i-2*k]
        return PreSum

        # PreSum = self.PreSumFunction(mat, k)
        # Answer = [[0]*self.row for _ in range(self.col)]
        # print(PreSum)
        # for i in range(self.row):
        #     for j in range(self.col):
        #         if i==0 and j==0:
        #             print("test")
        #             print(i,j,k)
        #             print(PreSum[i+k][j+k])
        #             print(PreSum[i-k][j-k])
        #             print(PreSum[i-k][j])
        #             print(PreSum[i][j-k])
        #         # Answer[i][j] = PreSum[i+k][j+k] + PreSum[i-k][j-k] - PreSum[i-k][j] - PreSum[i][j-k] 
        #         Answer[i][j] = PreSum[i+k][j+k] + PreSum[i][j] - PreSum[i][j+k] - PreSum[i+k][j]
        #         # Answer[i][j] = PreSum[i+k][j+k] + PreSum[i+k-1][j+k-1] - PreSum[i+k-1][j+k] - PreSum[i+k][j+k-1]
        #         return Answer