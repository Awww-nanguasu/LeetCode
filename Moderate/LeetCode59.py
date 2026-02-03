class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[1]*n for _ in range(n)]
        right = n-1
        left = n-1
        lower = n-1
        upper = n-2
        i, j = 0, 0
        val = 1
        while(right > 0 or upper > 0 or lower > 0):
            for k in range(right):
                j = j + 1
                matrix[i][j] = val
                val = val + 1
            
            right = right - 1
            
            for k in range(lower):
                i = i + 1
                matrix[i][j] = val
                val = val + 1
            
            lower = lower - 1

            for k in range(left):
                j = j - 1
                matrix[i][j] = val
                val = val + 1
            
            left = left - 1

            for k in range(upper):
                i = i - 1
                matrix[i][j] = val
                val = val + 1
            
            upper = upper - 1
        return matrix