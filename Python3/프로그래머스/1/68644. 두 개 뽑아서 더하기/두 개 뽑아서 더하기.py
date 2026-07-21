def solution(numbers):
    
    result = set()
    
    for i in range(len(numbers)):
        for j in range(1, len(numbers)-i):
            result.add(numbers[i]+numbers[i+j])

    answer = list(result)
    answer.sort()
    return answer