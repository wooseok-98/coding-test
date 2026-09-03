from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    dist = [[-1]*m for _ in range(n)]
    dq = deque([(0,0)])
    
    dist[0][0] = 1
    
    while dq:
        x, y = dq.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if not ( 0 <= nx < n and 0 <= ny < m):
                continue
            if dist[nx][ny] != -1:
                continue
            if maps[nx][ny] == 0:
                continue
            dist[nx][ny] = dist[x][y] + 1
            dq.append((nx, ny))
    
    
    return dist[n-1][m-1]