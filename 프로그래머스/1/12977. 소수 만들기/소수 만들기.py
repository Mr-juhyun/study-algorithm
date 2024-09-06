from itertools import combinations
def solution(nums):
    
    def find_sosu(num):
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    all_nums = combinations(nums,3)
    target = [sum(num_list) for num_list in all_nums]
    answer = 0
    
    for num in target:
        if find_sosu(num):
            answer += 1
    return answer
        
    
    
    return 0