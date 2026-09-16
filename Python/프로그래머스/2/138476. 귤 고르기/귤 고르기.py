from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    size = Counter(tangerine)
    
    for _, v in size.most_common():
        answer += 1
        k -= v
        if k <= 0:
            break
            
    return answer