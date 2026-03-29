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