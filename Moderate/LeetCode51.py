class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n + 1)]
        def dfs(path, begin):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if is_valid(begin, i):
                    board[begin][i] = 'Q'
                    # add_path = '.' * i + 'Q' +'.' * (n - 1 - i)
                    path.append(''.join(board[begin]))
                    dfs(path, begin + 1)
                    path.pop()
                    board[begin][i] = '.'
        def is_valid(x, y):

            for i in range(x):
                if board[i][y] == 'Q':
                    return False

            for i in range(x):
                if x + y - i < n and board[i][x + y - i] == 'Q':
                    return False

            for i in range(x):
                if x - 1 - i >= 0 and y - 1 - i >= 0 and board[x - 1 - i][y - 1 - i] == 'Q':
                    return False
            return True
        
        dfs([], 1)
        return res

