from collections import Counter
def solution(want, number, discount):
    s = 0
    dis_lst = discount[s:s+10]
    answer = 0
    want = {want[i]:number[i] for i in range(len(want))}
    
    while len(dis_lst) == 10:
        if want == Counter(dis_lst):
            answer += 1
        s += 1
        dis_lst = discount[s:s+10]
        
    return answer