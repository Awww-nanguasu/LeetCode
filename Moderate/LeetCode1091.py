class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        if n == 1:
            return 1
        
        q = deque([(0, 0, 1)])
        grid[0][0] = 1
        nx = [0, 0, 1, 1, 1, -1, -1, -1]
        ny = [1, -1, 0, 1, -1, 0, 1, -1]
        while q:
            (x, y, step) = q.popleft()
            for k in range(8):
                dx = x + nx[k]
                dy = y + ny[k]
                if 0 <= dx <= n-1 and 0 <= dy <= n-1 and grid[dx][dy] == 0:
                    if dx == n-1 and dy == n-1:
                        return step + 1

                    if grid[dx][dy] == 0:
                        grid[dx][dy] = 1
                        q.append((dx, dy, step+1))
        return -1