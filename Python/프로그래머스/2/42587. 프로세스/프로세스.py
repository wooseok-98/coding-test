from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    answer = 0

    while queue:
        p = queue.popleft()
        if any(p[1] < q[1] for q in queue):
            queue.append(p)
        else:
            answer += 1
            if p[0] == location:
                return answer
