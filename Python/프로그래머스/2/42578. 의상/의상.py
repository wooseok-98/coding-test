def solution(clothes):
    
    closet = {}
    
    for c in clothes:
        cloth_list = []
        closet[c[1]] = closet.get(c[1], cloth_list)
        closet[c[1]].append(c[0])
        
    answer = 1
    for key, value in closet.items():
        answer *= len(value)+1
    
    return answer - 1