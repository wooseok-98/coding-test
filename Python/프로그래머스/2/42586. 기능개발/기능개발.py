from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    work_day = deque()
    for i in range(len(progresses)):
        work_day.append((math.ceil((100-progresses[i])/speeds[i])))

    while(work_day):
        current_day = work_day.popleft()
        count = 1
        while work_day and work_day[0] <= current_day:
            work_day.popleft()
            count += 1
        answer.append(count)
    
    return answer