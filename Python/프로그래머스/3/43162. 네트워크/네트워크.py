from collections import deque

def solution(n, computers):
    
    visited = [False] * n
    
    def bfs(start):
        dq = deque([start])
        visited[start] = True
        while dq:
            cur = dq.popleft()
            for nx in range(n):
                if computers[cur][nx] == 0: continue
                if visited[nx]: continue
                visited[nx] = True
                dq.append(nx)
    count = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            count += 1
    
    return count