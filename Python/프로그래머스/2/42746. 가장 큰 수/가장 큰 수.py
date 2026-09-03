def solution(numbers):
    
    arr = [str(n) for n in numbers]

    arr.sort(key = lambda x : x*3, reverse=True)
    
    answer = ''.join(arr)

    if answer[0] == '0':
        return '0'
        
    return answer
