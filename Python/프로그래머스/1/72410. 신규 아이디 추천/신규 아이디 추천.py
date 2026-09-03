def solution(new_id):
        
    # 1단계
    id_1 = new_id.lower()
    
    # 2단계
    answer = ""
    for c in id_1:
        if c.islower() or c.isdigit() or c == "-" or c == "_" or c == ".":
            answer += c
            
    # 3단계
    while ".." in answer:
        answer = answer.replace("..", ".")
        
    # 4단계
    if answer[0] == "." and len(answer)>1:
        answer = answer[1:]
    if answer[-1] == ".":
        answer = answer[:-1]
        
    # 5단계
    if not(answer):
        answer = "a"
        
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
            
    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
            
    return answer