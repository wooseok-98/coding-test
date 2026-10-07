from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((i,p))
    
    while queue:
        w = queue.popleft()
        if any(w[1] < q[1] for q in queue):
            queue.append(w)
        else:
            answer += 1
            if w[0] == location:
                return answer
