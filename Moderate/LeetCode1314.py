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