def solution(n, t, m, p):
    answer = ""
    num = 0
    need_nums = ""
    need_nums_len = t*m
    
    def base_con(num,base):
        to_base = "0123456789ABCDEF"
        
        if num == 0:
            return "0"
        result = ""
        
        while num > 0:
            result = to_base[num%base] + result
            num //= base
        return result
    
    while len(need_nums) < need_nums_len:
        need_nums += base_con(num,n)
        num += 1
    
    for idx,num in enumerate(need_nums):
        if idx%m +1 == p:
            answer+= num
        if len(answer) == t:
            break
        
    return answer 