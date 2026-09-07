from collections import Counter

def solution(s):
    answer = []
    
    n = s.replace('{','').replace('}', '')
    nums = n.split(',')
    c = Counter(nums)
    
    for k, v in c.most_common():
        answer.append(int(k))

    return answer