class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        chess = [['.' for _ in range(n)] for _ in range(n)]  # 初始化棋盘
        ans = 0

        def dfs(row: int, chess: list[list[str]]):
            nonlocal ans
            if row == n:  
                ans += 1
                return
            for col in range(n):
                if is_valid(row, col, chess):
                    chess[row][col] = 'Q'  
                    dfs(row + 1, chess) 
                    chess[row][col] = '.' 

        def is_valid(row: int, col: int, chess: list[list[str]]) -> bool:
            for i in range(row):  
                if chess[i][col] == 'Q':
                    return False

            for j in range(col):
                if chess[row][j] == 'Q':
                    return False

            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if chess[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if chess[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True 

        dfs(0, chess)
        return ans


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        chess = [['.' for _ in range(n)] for _ in range(n)]  # 初始化棋盘
        ans = 0

        def dfs(row: int, chess: list[list[str]]):
            nonlocal ans
            if row == n:  
                ans += 1
                return
            for col in range(n):
                if is_valid(row, col, chess):
                    chess[row][col] = 'Q'  
                    dfs(row + 1, chess) 
                    chess[row][col] = '.' 

        def is_valid(row: int, col: int, chess: list[list[str]]) -> bool:
            for i in range(row):  
                if chess[i][col] == 'Q':
                    return False

            for j in range(col):
                if chess[row][j] == 'Q':
                    return False

            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if chess[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if chess[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True 

        dfs(0, chess)
        return ans

