from itertools import permutations
from math import sqrt
def solution(numbers):
    len_num = len(numbers)
    numbers = [n for n in numbers]
    p_num = set()
    answer = 0
    for i in range(1,len_num+1):
        for nums in list(permutations(numbers,i)):
            temp = ''
            for num in nums:
                temp+= num
            if int(temp) > 1:
                p_num.add(int(temp))
    for p in p_num:
        check = True
        for i in range(2,int(sqrt(p))+1):
            if p%i == 0:
                check = False
                break
        if check:
            print(p)
            answer+=1
    return answer