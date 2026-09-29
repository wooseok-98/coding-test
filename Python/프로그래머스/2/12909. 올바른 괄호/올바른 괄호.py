def solution(s):
    answer = True
    stack = []
    
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                answer = False
            else:
                stack.pop()
            
    if stack:
        answer = False
    
    return answer