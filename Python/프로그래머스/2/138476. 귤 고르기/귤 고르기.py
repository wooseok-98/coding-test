from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    size = Counter()
    for t in tangerine:
        size[t] = size.get(t, 0) + 1
    
    for _, v in size.most_common():
        if v >= k:
            answer += 1
            break
        else:
            k = k - v
            if k > 0:
                answer += 1
            else:
                break
            
    return answer