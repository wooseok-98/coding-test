def solution(answers):
    
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    result = [0]*3
    
    for i in range(len(answers)):
        if p1[i%5] == answers[i]:
            result[0] += 1
        if p2[i%8] == answers[i]:
            result[1] += 1
        if p3[i%10] == answers[i]:
            result[2] += 1
    
    answer = []
    for idx, score in enumerate(result):
        if score == max(result):
            answer.append(idx+1)
    
    return answer