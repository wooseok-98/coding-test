def solution(n):

    # map, reversed 사용
    answer = list(map(int, reversed(str(n))))
    
    return answer