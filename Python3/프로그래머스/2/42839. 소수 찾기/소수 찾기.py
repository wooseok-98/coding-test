from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def make_num(s):
    nums = set()
    
    for r in range(1, len(s)+1):
        for combo in permutations(s, r):
            nums.add(int(''.join(combo)))
        
    return nums
    
def solution(numbers):
    answer = 0
    nums = make_num(numbers)
    
    for n in nums:
        if is_prime(n) == True:
            answer += 1
    
    return answer