def solution(nums):
    
    get_num = len(nums)//2
    type_num = len(set(nums))
    
    answer = min(get_num, type_num)
    return answer
