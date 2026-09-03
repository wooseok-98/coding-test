from collections import Counter

def solution(array):
    
    # 빈도수 내림차순 정렬
    counts = Counter(array).most_common()
    
    if len(counts) == 1:
        answer = counts[0][0]
    else:
        if counts[0][1] != counts [1][1]:
            answer = counts[0][0]
        else:
            answer = -1
            
    return answer