from collections import deque

def solution(s):
    answer = True
    q = deque()
    
    for c in s:
        if c == ")":
            if not q:
                answer = False
                break
            else:
                q.popleft()
        else:
            q.append(c)
            
    if q:
        answer = False

    return answer