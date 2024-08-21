from collections import defaultdict, OrderedDict
def solution(n, works):
    work = defaultdict(int)
    total = 0
    answer= 0
    for i in works:
        work[i] += 1
        total += i
        
    if total <= n:
        return 0
    
    max_work = max(work)
    while n:
        target = work.pop(max_work) 
        if target > n:
            work[max_work] = target-n
            work[max_work-1] += n
            break
        n -= target
        work[max_work-1] += target
        max_work -= 1
    for idx in work:
        answer += idx**2 * work[idx]
    return answer





