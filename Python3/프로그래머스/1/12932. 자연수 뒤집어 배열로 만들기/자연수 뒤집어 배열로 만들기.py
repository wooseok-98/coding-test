def solution(n):
    answer = []
    
    c = str(n)
    
    for i in range(0, len(c)):
        idx = len(c) - i - 1
        answer.append(int(c[idx]))
    
    return answer