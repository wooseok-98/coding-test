def solution(numbers):
    
    nums = [0,1,2,3,4,5,6,7,8,9]
    
    none = set(nums)-set(numbers)
    
    answer = sum(none)
    return answer