class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while q:
            cx, cy, d = q.popleft()
            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and maze[nx][ny] == '.':
                    if nx == 0 or nx == n - 1 or ny == 0 or ny == m - 1:
                        return d + 1
                    
                    maze[nx][ny] = '+'
                    q.append((nx, ny, d + 1))
        return -1
