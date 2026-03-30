class Solution:
    def __init__(self):
        self.hashmap = []

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def bfs(row, col, n, m, step):
            #把判断加到循环里
            if maze[row][col]=='+':
                return 10000

            if row>0 and [row-1, col] not in self.hashmap and maze[row-1][col]=='.' and row-1==0:
                step += 1
                return step
            
            if row<n and [row+1, col] not in self.hashmap and maze[row+1][col]=='.'  and row+1==n:
                step += 1
                return step

            if col>0 and [row, col-1] not in self.hashmap and maze[row][col-1]=='.' and col-1==0:
                step += 1
                return step

            if col<m and [row, col+1] not in self.hashmap and maze[row][col+1]=='.' and col+1==m:
                step += 1
                return step

            self.hashmap.append([row-1, col])
            self.hashmap.append([row+1, col])
            self.hashmap.append([row, col-1])
            self.hashmap.append([row, col+1])

            step += 1
            up = bfs(row-1, col, n, m, step)
            down = bfs(row+1, col, n, m, step)
            left = bfs(row, col-1, n, m, step)
            right =bfs(row, col+1, n, m, step)

            return min(up, down, left, right)
        
        n = len(maze) - 1
        m = len(maze[0]) - 1
        step = 0
        step = bfs(entrance[0], entrance[1], n, m, step)
        if step>=10000:
            return -1
        
        return step
    
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        # 上下左右四个相邻坐标对应的行列变化量
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        # 入口加入队列并修改为墙
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            cx, cy, d = q.popleft()
            # 遍历四个方向相邻坐标
            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    # 新坐标合法且不为墙
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        # 新坐标为出口，返回距离作为答案
                        return d + 1
                    # 新坐标为空格子且不为出口，修改为墙并加入队列
                    maze[nx][ny] = '+'
                    q.append((nx, ny, d + 1))
        # 不存在到出口的路径，返回 -1
        return -1
