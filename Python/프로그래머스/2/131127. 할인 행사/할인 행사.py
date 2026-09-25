from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    # 구매 항목+수량
    shop = {}
    for i, w in enumerate(want):
        shop[w] = number[i]
    
    for i in range(len(discount)-9):
        day_discount = Counter(discount[i:i+10])
        if shop == day_discount:
            answer += 1
    
    return answer