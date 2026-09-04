from collections import deque

def solution(n, computers):
    
    visited = [False]*n
    
    def bfs(start):
        dq = deque([start])
        visited[start] = True
        while dq:
            cur = dq.popleft()
            for nxt in range(n):
                if computers[cur][nxt] == 0: continue
                if visited[nxt]: continue
                visited[nxt] = True
                dq.append(nxt)
                
    count = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            count += 1
    
    return count