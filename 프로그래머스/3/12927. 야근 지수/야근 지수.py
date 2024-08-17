from collections import Counter
def solution(n, works):
    if sum(works) <= n:
        return 0
    answer = 0
    works = Counter(works)
    max_work = max(works)
    while n >0:
        target = works.pop(max_work) 
        if target > n:
            works[max_work] = target-n
            works[max_work-1] += n
            break
        else:
            n -= target
            works[max_work-1] += target
            max_work -= 1
    for work in works:
        answer += work**2 * works[work]
    return answer




