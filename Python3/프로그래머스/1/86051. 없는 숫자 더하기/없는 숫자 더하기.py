def solution(numbers):
    
    nums = range(10)
    
    none = set(nums)-set(numbers)
    
    answer = sum(none)
    return answer