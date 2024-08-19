from collections import Counter

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    work_counts = Counter(works)
    max_work = max(work_counts)
    
    while n > 0 and max_work > 0:
        count = work_counts[max_work]
        

        if count > n:
            work_counts[max_work] -= n
            work_counts[max_work - 1] += n
            break

        work_counts[max_work - 1] += count
        n -= count
        del work_counts[max_work] 
        max_work -= 1 
    
    return sum(work ** 2 * count for work, count in work_counts.items())

